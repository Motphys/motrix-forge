/* Apply before styles load to avoid a white flash when opening a dark page. */
(() => {
  "use strict";
  const key = "forge-docs-theme";
  const root = document.documentElement;
  const system = window.matchMedia("(prefers-color-scheme: dark)");
  let preference = null;
  try { preference = localStorage.getItem(key); } catch { /* Storage may be unavailable. */ }
  const valid = value => value === "light" || value === "dark";
  const apply = () => {
    const dark = (valid(preference) ? preference : system.matches ? "dark" : "light") === "dark";
    root.dataset.theme = dark ? "dark" : "light";
    const chinese = root.lang === "zh-CN";
    document.querySelectorAll("[data-theme-toggle]").forEach(button => {
      const action = chinese ? (dark ? "切换至浅色主题" : "切换至黑色主题") : (dark ? "Switch to light theme" : "Switch to dark theme");
      button.setAttribute("aria-pressed", String(dark));
      button.setAttribute("aria-label", action);
      button.title = action;
      button.querySelector(".theme-label").textContent = chinese ? (dark ? "黑色主题" : "浅色主题") : (dark ? "Dark theme" : "Light theme");
    });
  };
  apply();
  document.addEventListener("DOMContentLoaded", () => {
    apply();
    document.querySelectorAll("[data-theme-toggle]").forEach(button => {
      button.addEventListener("click", () => {
        preference = root.dataset.theme === "dark" ? "light" : "dark";
        try { localStorage.setItem(key, preference); } catch { /* Keep working without persistence. */ }
        apply();
      });
    });
  });
  system.addEventListener("change", () => { if (!valid(preference)) apply(); });
  window.addEventListener("storage", event => {
    if (event.key === key || event.key === null) {
      preference = event.newValue;
      apply();
    }
  });
})();
