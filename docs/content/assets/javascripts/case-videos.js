/* Keep case study covers clean until the visitor starts playback. */
(() => {
  "use strict";
  const chinese = document.documentElement.lang === "zh-CN";
  document.querySelectorAll("video[data-click-to-play]").forEach(video => {
    const wrapper = document.createElement("div");
    wrapper.className = "case-video";
    video.before(wrapper);
    wrapper.append(video);

    const start = document.createElement("button");
    start.type = "button";
    start.className = "case-video-start";
    const icon = document.createElement("span");
    icon.className = "case-video-play-icon";
    icon.setAttribute("aria-hidden", "true");
    start.append(icon);
    const title = video.getAttribute("aria-label") || "";
    start.setAttribute("aria-label", `${chinese ? "播放视频" : "Play video"}: ${title}`);
    wrapper.append(start);
    video.controls = false;
    const status = document.createElement("p");
    status.className = "case-video-status";
    status.setAttribute("role", "status");
    status.hidden = true;
    wrapper.append(status);
    let prepared = false;
    let objectURL = null;
    const prepare = async () => {
      if (prepared) return;
      const url = video.currentSrc || video.querySelector("source")?.src || video.src;
      // Some static hosts ignore Range. Reuse their full response as a local
      // Blob, which lets the native player seek without further HTTP requests.
      let response = await fetch(url, { headers: { Range: "bytes=0-0" } });
      if (response.status === 206 && /^bytes 0-0\/\d+$/.test(response.headers.get("Content-Range") || "")) {
        await response.body?.cancel();
      } else {
        if (response.status === 206) {
          await response.body?.cancel();
          response = await fetch(url);
        }
        if (response.status !== 200) throw new Error(`Video request failed: ${response.status}`);
        const blob = await response.blob();
        if (!blob.size) throw new Error("Empty video response");
        objectURL = URL.createObjectURL(blob);
        video.src = objectURL;
        video.load();
      }
      prepared = true;
    };
    window.addEventListener("pagehide", event => {
      if (!event.persisted && objectURL) URL.revokeObjectURL(objectURL);
    });

    const reveal = () => {
      video.controls = true;
      start.hidden = true;
    };
    video.addEventListener("play", reveal);
    start.addEventListener("click", async event => {
      event.preventDefault();
      if (start.disabled) return;
      start.disabled = true;
      start.setAttribute("aria-busy", "true");
      status.textContent = chinese ? "正在加载视频…" : "Loading video…";
      status.hidden = false;
      try {
        await prepare();
      } catch {
        status.textContent = chinese ? "视频加载失败，请点击播放按钮重试。" : "Video could not load. Click the play button to retry.";
        start.disabled = false;
        start.removeAttribute("aria-busy");
        return;
      }
      status.hidden = true;
      start.disabled = false;
      start.removeAttribute("aria-busy");
      reveal();
      video.focus({ preventScroll: true });
      try {
        await video.play();
      } catch {
        // Retain native controls for retry or a browser-provided error message.
        video.controls = true;
      }
    });
  });
})();
