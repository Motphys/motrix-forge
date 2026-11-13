/* Navigation and language-scoped search for the static manual. */
(() => {
  "use strict";
  const chinese = document.documentElement.lang === "zh-CN";
  // Sidebar groups were restored before its first paint. Initialize any
  // collapsible chapter list in the article without resetting the sidebar.
  window.forgeRestoreNavigationGroups?.(document);
  const toggle = document.querySelector(".menu-toggle");
  const sidebar = document.querySelector(".manual-sidebar");
  const outlineToggle = document.querySelector(".outline-toggle");
  const outlinePanel = document.querySelector(".page-outline");
  const narrow = window.matchMedia("(max-width: 1520px)");
  let activeDrawer = null;
  const panels = { sidebar, outline: outlinePanel };
  const triggers = { sidebar: toggle, outline: outlineToggle };
  const focusable = 'a[href], button, input, summary, [tabindex="0"]';
  const setDrawer = (name, restoreFocus = true) => {
    const previous = activeDrawer;
    activeDrawer = narrow.matches && panels[name] ? name : null;
    for (const key of ["sidebar", "outline"]) {
      const open = activeDrawer === key;
      document.body.classList.toggle(`${key}-open`, open);
      triggers[key]?.setAttribute("aria-expanded", String(open));
      if (panels[key]) panels[key].inert = narrow.matches && !open;
    }
    if (activeDrawer) panels[activeDrawer].querySelector(focusable)?.focus({ preventScroll: true });
    else if (previous && restoreFocus && narrow.matches) triggers[previous]?.focus();
  };
  setDrawer(null);
  narrow.addEventListener("change", () => setDrawer(null));
  toggle?.addEventListener("click", () => setDrawer(activeDrawer === "sidebar" ? null : "sidebar"));
  outlineToggle?.addEventListener("click", () => setDrawer(activeDrawer === "outline" ? null : "outline"));
  document.querySelector(".sidebar-backdrop")?.addEventListener("click", () => setDrawer(null));
  document.querySelector(".outline-close")?.addEventListener("click", () => setDrawer(null));
  outlinePanel?.addEventListener("click", event => {
    if (narrow.matches && event.target.closest("a[href]")) {
      setDrawer(null, false);
      document.getElementById("main-content")?.focus({ preventScroll: true });
    }
  });
  document.addEventListener("keydown", event => {
    if (event.key === "Escape") {
      setDrawer(null);
      document.querySelectorAll(".language-switch[open]").forEach(details => details.open = false);
    }
    if (event.key === "Tab" && activeDrawer) {
      const controls = [...panels[activeDrawer].querySelectorAll(focusable)].filter(element => element.getClientRects().length);
      const first = controls[0], last = controls[controls.length - 1];
      if ((event.shiftKey && document.activeElement === first) || (!event.shiftKey && document.activeElement === last)) {
        event.preventDefault();
        (event.shiftKey ? last : first)?.focus();
      }
    }
  });
  document.querySelectorAll(".manual-article table").forEach(table => {
    const wrapper = document.createElement("div");
    wrapper.className = "table-scroll";
    wrapper.tabIndex = 0;
    wrapper.setAttribute("role", "region");
    wrapper.setAttribute("aria-label", chinese ? "表格，可水平滚动" : "Table, scroll horizontally");
    table.before(wrapper);
    wrapper.append(table);
  });
  const outline = [...document.querySelectorAll(".page-outline a")];
  if ("IntersectionObserver" in window) {
    const observer = new IntersectionObserver(entries => {
      const visible = entries.filter(entry => entry.isIntersecting);
      if (!visible.length) return;
      const id = visible[0].target.id;
      outline.forEach(link => link.classList.toggle("active", decodeURIComponent(link.hash.slice(1)) === id));
    }, { rootMargin: "-5% 0px -70% 0px" });
    outline.forEach(link => {
      const heading = document.getElementById(decodeURIComponent(link.hash.slice(1)));
      if (heading) observer.observe(heading);
    });
  }
  // MkDocs' worker indexes both languages; show only the current language.
  if (typeof window.displayResults === "function") {
    const display = window.displayResults;
    window.displayResults = results => display(results.filter(result => {
      const path = result.location.split("#")[0];
      const isChinese = path.startsWith("cn/") || path.includes(".zh-CN.");
      return chinese === isChinese;
    }));
  }
  if (document.getElementById("mkdocs-search-query")) {
    document.querySelectorAll(".language-options a, .mobile-header a[lang]").forEach(link => {
      if (!link.href.includes("search.html")) return;
      const url = new URL(link.href);
      const query = new URLSearchParams(location.search).get("q");
      if (query) url.searchParams.set("q", query);
      link.href = url.href;
    });
  }
})();
