(() => {
  'use strict';

  const tabs = [...document.querySelectorAll('[role="tab"]')];
  const activateTab = (tab, focus = false) => {
    tabs.forEach((item) => {
      const selected = item === tab;
      item.setAttribute('aria-selected', String(selected));
      item.tabIndex = selected ? 0 : -1;
      document.getElementById(item.getAttribute('aria-controls')).hidden = !selected;
    });
    if (focus) tab.focus();
  };
  tabs.forEach((tab, index) => {
    tab.addEventListener('click', () => activateTab(tab));
    tab.addEventListener('keydown', (event) => {
      let next;
      if (event.key === 'ArrowRight') next = (index + 1) % tabs.length;
      if (event.key === 'ArrowLeft') next = (index + tabs.length - 1) % tabs.length;
      if (event.key === 'Home') next = 0;
      if (event.key === 'End') next = tabs.length - 1;
      if (next === undefined) return;
      event.preventDefault();
      activateTab(tabs[next], true);
    });
  });

  const sceneImage = document.getElementById('scene-image');
  const sceneLink = document.getElementById('scene-link');
  const sceneCaption = document.getElementById('scene-caption');
  const sceneButtons = [...document.querySelectorAll('[data-scene]')];
  sceneButtons.forEach((button) => button.addEventListener('click', () => {
    sceneButtons.forEach((item) => item.setAttribute('aria-pressed', String(item === button)));
    sceneImage.src = button.dataset.scene;
    sceneImage.alt = button.dataset.sceneCaption;
    sceneLink.href = button.dataset.scene;
    sceneLink.dataset.caption = button.dataset.sceneCaption;
    sceneCaption.textContent = button.dataset.sceneCaption;
  }));

  const dialog = document.getElementById('image-dialog');
  const dialogImage = document.getElementById('dialog-image');
  const dialogCaption = document.getElementById('dialog-caption');
  const dialogOriginal = document.getElementById('dialog-original');
  let previousFocus = null;
  document.querySelectorAll('[data-lightbox]').forEach((link) => {
    link.addEventListener('click', (event) => {
      if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey || typeof dialog.showModal !== 'function') return;
      event.preventDefault();
      previousFocus = link;
      dialogImage.src = link.href;
      dialogImage.alt = link.querySelector('img')?.alt || link.dataset.caption;
      dialogCaption.textContent = link.dataset.caption;
      dialogOriginal.href = link.href;
      dialog.showModal();
      document.body.style.overflow = 'hidden';
    });
  });
  document.querySelector('.dialog-close').addEventListener('click', () => dialog.close());
  dialog.addEventListener('click', (event) => {
    if (event.target !== dialog) return;
    const bounds = dialog.getBoundingClientRect();
    if (event.clientX < bounds.left || event.clientX > bounds.right || event.clientY < bounds.top || event.clientY > bounds.bottom) dialog.close();
  });
  dialog.addEventListener('close', () => {
    document.body.style.overflow = '';
    dialogImage.removeAttribute('src');
    previousFocus?.focus({preventScroll: true});
  });

  const navLinks = [...document.querySelectorAll('.nav-inner a')];
  const chapters = navLinks.map((link) => document.querySelector(link.hash));
  const progress = document.querySelector('.reading-progress span');
  let scrollQueued = false;
  const updateReading = () => {
    scrollQueued = false;
    let current = chapters[0];
    chapters.forEach((chapter) => {
      if (chapter.getBoundingClientRect().top <= 150) current = chapter;
    });
    navLinks.forEach((link) => {
      if (link.hash === '#' + current.id) link.setAttribute('aria-current', 'location');
      else link.removeAttribute('aria-current');
    });
    const maximum = document.documentElement.scrollHeight - window.innerHeight;
    progress.style.width = (maximum > 0 ? Math.min(100, Math.max(0, window.scrollY / maximum * 100)) : 0) + '%';
  };
  const queueReading = () => {
    if (scrollQueued) return;
    scrollQueued = true;
    window.requestAnimationFrame(updateReading);
  };
  window.addEventListener('scroll', queueReading, {passive: true});
  window.addEventListener('resize', queueReading);
  window.addEventListener('load', queueReading);
  updateReading();
  document.querySelector('[data-print]').addEventListener('click', () => window.print());
})();
