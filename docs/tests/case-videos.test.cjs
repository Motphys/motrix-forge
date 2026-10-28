const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

const code = fs.readFileSync(path.join(__dirname, '../content/assets/javascripts/case-videos.js'), 'utf8');

function setup(responses, rejectPlay = false) {
  class Element {
    constructor() { this.events = {}; this.hidden = false; this.attributes = {}; this.disabled = false; this.children = []; }
    before() {}
    append(element) { this.children.push(element); }
    after(element) { this.afterElement = element; }
    setAttribute(key, value) { this.attributes[key] = value; }
    getAttribute(key) { return this.attributes[key] || ''; }
    removeAttribute(key) { delete this.attributes[key]; }
    addEventListener(name, fn) { this.events[name] = fn; }
    querySelector() { return { src: 'https://example.test/assets/video.mp4' }; }
    load() { this.loaded = true; }
    focus() {}
    async play() { if (rejectPlay) throw Error('gesture required'); this.played = true; }
  }
  const video = new Element();
  const elements = [];
  const requests = [];
  const blobs = [];
  const revoked = [];
  const window = new Element();
  vm.runInNewContext(code, {
    document: {
      documentElement: { lang: 'en' }, querySelectorAll: () => [video],
      createElement: () => { const element = new Element(); elements.push(element); return element; },
    },
    window,
    fetch: async (...args) => { requests.push(args); if (!responses.length) throw Error('offline'); return responses.shift(); },
    URL: { createObjectURL: blob => { blobs.push(blob); return 'blob:video'; }, revokeObjectURL: url => revoked.push(url) },
  });
  const button = elements[1];
  const click = () => button.events.click({ preventDefault() {} });
  return { video, wrapper: elements[0], button, click, status: elements[3], requests, blobs, revoked, window };
}

test('Range host uses normal streaming and enables native controls', async () => {
  const app = setup([new Response('x', { status: 206, headers: { 'Content-Range': 'bytes 0-0/100' } })]);
  assert.equal(app.video.controls, false);
  await app.click();
  assert.equal(app.video.played, true);
  assert.equal(app.video.controls, true);
  assert.equal(app.button.hidden, true);
  assert.equal(app.blobs.length, 0);
});

test('Host ignoring Range uses complete local video for seeking', async () => {
  const app = setup([new Response('complete video', { headers: { 'Content-Type': 'video/mp4' } })]);
  await app.click();
  assert.equal(await app.blobs[0].text(), 'complete video');
  assert.equal(app.video.src, 'blob:video');
  assert.equal(app.video.loaded, true);
  assert.equal(app.video.played, true);
  assert.equal(app.requests.length, 1);
  app.window.events.pagehide({ persisted: true });
  assert.equal(app.revoked.length, 0);
  app.window.events.pagehide({ persisted: false });
  assert.deepEqual(app.revoked, ['blob:video']);
});

test('Unexpected partial response downloads a full representation', async () => {
  const app = setup([new Response('x', { status: 206 }), new Response('full video')]);
  await app.click();
  assert.equal(app.requests.length, 2);
  assert.equal(app.requests[1][1], undefined);
  assert.equal(await app.blobs[0].text(), 'full video');
});

test('Failed loading keeps cover and allows retry', async () => {
  const app = setup([new Response('', { status: 404 })]);
  await app.click();
  assert.equal(app.button.hidden, false);
  assert.equal(app.button.disabled, false);
  assert.equal(app.video.controls, false);
  assert.match(app.status.textContent, /retry/);
});

test('Browser playback rejection leaves native controls usable', async () => {
  const app = setup([new Response('video')], true);
  await app.click();
  assert.equal(app.video.controls, true);
  assert.equal(app.button.hidden, true);
});

test('Loading status stays inside the fixed video frame', () => {
  const app = setup([]);
  assert.ok(app.wrapper.children.includes(app.status));
});
