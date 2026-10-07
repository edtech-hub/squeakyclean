(function () {
  var header = document.querySelector('.site-header');
  var toggle = document.querySelector('.menu-toggle');
  toggle.addEventListener('click', function () {
    var open = header.classList.toggle('open');
    toggle.setAttribute('aria-expanded', open);
    toggle.textContent = open ? 'Close' : 'Menu';
  });
  document.querySelectorAll('#nav a').forEach(function (a) {
    a.addEventListener('click', function () { header.classList.remove('open'); toggle.setAttribute('aria-expanded', false); toggle.textContent = 'Menu'; });
  });

  // Fade-ins
  var items = document.querySelectorAll('.wp-reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -8% 0px' });
    items.forEach(function (el, i) { el.style.transitionDelay = (i % 5) * 70 + 'ms'; io.observe(el); });
  } else { items.forEach(function (el) { el.classList.add('is-in'); }); }

  // Mobile action bar appears once the hero buttons scroll away
  var bar = document.querySelector('.mobile-bar'), ctas = document.getElementById('hero-ctas');
  if (bar && ctas && 'IntersectionObserver' in window) {
    new IntersectionObserver(function (es) { bar.classList.toggle('show', !es[0].isIntersecting && es[0].boundingClientRect.top < 0); }).observe(ctas);
  }

  // Service links pre-select the estimate form
  var form = document.querySelector('[data-form="estimate"]');
  function pick(v) { var r = form.querySelector('input[name="service"][value="' + v + '"]'); if (r) r.checked = true; }
  document.querySelectorAll('[data-service]').forEach(function (a) { a.addEventListener('click', function () { pick(a.dataset.service); }); });
  var qs = new URLSearchParams(location.search).get('service'); if (qs) pick(qs);

  // Gravity-style validation. Sends nothing: the form service is wired in after the deal closes.
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var bad = false;
    form.querySelectorAll('.gfield_validation_message').forEach(function (m) { m.remove(); });
    form.querySelectorAll('[required]').forEach(function (f) {
      var g = f.closest('.gfield'); g.classList.remove('gfield_error');
      var ok = f.value.trim() && (!f.pattern || new RegExp('^' + f.pattern + '$').test(f.value.trim()));
      if (!ok) { bad = true; g.classList.add('gfield_error'); var m = document.createElement('div'); m.className = 'gfield_validation_message'; m.textContent = f.value.trim() ? 'Please enter a 5-digit ZIP code.' : 'This field is required.'; g.appendChild(m); }
    });
    form.querySelector('.gform_validation_errors').hidden = !bad;
    if (bad) { form.querySelector('.gfield_error input').focus(); return; }
    var name = form.querySelector('#f-name').value.trim().split(' ')[0];
    form.innerHTML = '<h2 class="gform_title">Thanks, ' + name.replace(/[<>&"]/g, '') + '.</h2><p class="gform_confirmation_message">We got your request. Expect a call from us within 24 hours to set up your free estimate.</p><p class="gform_footer_note">Need us sooner? Call 817-938-7654.</p>';
  });

  // Easter egg: type "squeegee" or tap the logo five times for one streak-free pass.
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches, buf = '', taps = 0, tapT;
  function squeegee() {
    var t = document.createElement('div'); t.className = 'egg-toast'; t.textContent = 'Streak-free. If it rains in the next 3 days, we come back.';
    if (!reduce) { var p = document.createElement('div'); p.className = 'squeegee-pass'; document.body.appendChild(p); setTimeout(function () { p.remove(); }, 1400); }
    document.body.appendChild(t); setTimeout(function () { t.remove(); }, 3200);
  }
  document.addEventListener('keydown', function (e) {
    if (/input|textarea/i.test(e.target.tagName)) return;
    buf = (buf + (e.key || '')).slice(-8).toLowerCase(); if (buf === 'squeegee') squeegee();
  });
  document.querySelector('.site-header .wp-block-site-logo').addEventListener('click', function () {
    taps++; clearTimeout(tapT); tapT = setTimeout(function () { taps = 0; }, 1500); if (taps === 5) { taps = 0; squeegee(); }
  });
  console.log('%cSqueaky Clean Windows', 'font:300 18px Georgia;color:#b7d4e8', '\nThis glass was wiped by White Phoenix Consulting.');
})();
