/* Native modal image preview; source Markdown and image dimensions stay intact. */
(() => {
  "use strict";
  const dialog = document.getElementById("image-preview");
  if (!dialog || typeof dialog.showModal !== "function") return;
  const preview = dialog.querySelector(".image-preview-image");
  const chinese = document.documentElement.lang === "zh-CN";
  let source = null;
  let readingPosition = null;
  const restorePosition = () => {
    if (readingPosition) window.scrollTo({ ...readingPosition, behavior: "instant" });
  };

  document.querySelectorAll(".manual-article img").forEach(image => {
    const link = image.closest("a");
    // Preserve images used as links to other documents or external pages.
    if (link && !/\.(avif|gif|jpe?g|png|svg|webp)$/i.test(new URL(link.href).pathname)) return;
    const trigger = link || image;
    const label = chinese ? "放大图片" : "Enlarge image";
    image.classList.add("zoomable-image");
    trigger.setAttribute("aria-haspopup", "dialog");
    if (!link) {
      image.tabIndex = 0;
      image.setAttribute("role", "button");
      image.setAttribute("aria-label", image.alt ? `${label}: ${image.alt}` : label);
    }
    if (!trigger.title) trigger.title = label;
    const open = event => {
      if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey || dialog.open || !image.naturalWidth) return;
      event.preventDefault();
      source = trigger;
      readingPosition = { left: window.scrollX, top: window.scrollY };
      preview.src = image.currentSrc || image.src;
      preview.alt = image.alt;
      document.documentElement.classList.add("image-preview-open");
      dialog.showModal();
      restorePosition();
    };
    trigger.addEventListener("click", open);
    if (!link) trigger.addEventListener("keydown", event => {
      if (event.key === "Enter" || event.key === " ") open(event);
    });
  });

  dialog.addEventListener("click", event => {
    if (event.target === dialog || event.target === preview) dialog.close();
  });
  // Native dialog handles Escape, keyboard focus containment, and the close form.
  dialog.addEventListener("close", () => {
    document.documentElement.classList.remove("image-preview-open");
    preview.removeAttribute("src");
    preview.alt = "";
    source?.focus({ preventScroll: true });
    restorePosition();
    source = null;
    readingPosition = null;
  });
})();
