/**
 * Sammy Sharp Oil & Gas — Universal Navigation Component
 * Injected into every page via <div id="nav-root"></div>
 * Active link is auto-detected from the current URL.
 */
(function () {
  const root = document.getElementById('nav-root');
  if (!root) return;

  const links = [
    { href: 'index.html',      label: 'HOME'       },
    { href: 'about.html',      label: 'ABOUT US'   },
    { href: 'operations.html', label: 'OPERATIONS' },
    { href: 'gallery.html',    label: 'GALLERY'    },
    { href: 'locate.html',     label: 'LOCATE US'  },
    { href: 'contact.html',    label: 'CONTACT'    },
    { href: 'teams.html',      label: 'TEAM'       },
  ];

  function isActive(href) {
    const path = window.location.pathname;
    const page = href.replace('.html', '');
    if (page === 'index' && (path === '/' || path.endsWith('/index.html') || path.endsWith('/'))) return true;
    if (page !== 'index' && (path.endsWith(href) || path.endsWith('/' + page) || path.endsWith('/' + page + '/'))) return true;
    return false;
  }

  function desktopLink(link) {
    const active = isActive(link.href);
    const cls = active
      ? 'text-amber-400 font-semibold'
      : 'text-zinc-300 hover:text-amber-400 transition-colors duration-200';
    return `<a href="${link.href}" class="${cls}">${link.label}</a>`;
  }

  function mobileLink(link) {
    const active = isActive(link.href);
    const cls = active
      ? 'text-amber-400 font-semibold'
      : 'text-zinc-300 hover:text-amber-400 transition-colors duration-200';
    return `<a href="${link.href}" onclick="closeMobileNav()" class="block py-3 border-b border-zinc-800 last:border-0 ${cls}">${link.label}</a>`;
  }

  root.innerHTML = `
    <nav class="bg-zinc-950 border-b border-zinc-800 fixed w-full z-50 top-0 left-0">
      <div class="max-w-7xl mx-auto px-4 sm:px-6">
        <div class="flex justify-between items-center h-20">

          <!-- Logo / Brand -->
          <a href="index.html" class="flex items-center gap-3 flex-shrink-0">
            <img src="logo.jpeg" alt="Sammy Sharp Oil and Gas Logo" class="h-10 w-auto object-contain">
            <div class="leading-tight">
              <span class="block text-base sm:text-lg font-bold tracking-tight text-white">SAMMY SHARP</span>
              <span class="block text-xs text-amber-400">OIL &amp; GAS LIMITED</span>
            </div>
          </a>

          <!-- Desktop Links (lg+) -->
          <div class="hidden lg:flex items-center gap-6 xl:gap-8 text-sm font-medium">
            ${links.map(desktopLink).join('\n            ')}
          </div>

          <!-- Hamburger (below lg) -->
          <button
            id="navToggleBtn"
            onclick="toggleMobileNav()"
            aria-label="Toggle navigation menu"
            aria-expanded="false"
            aria-controls="mobileNavMenu"
            class="lg:hidden flex items-center justify-center w-10 h-10 rounded-lg text-white hover:bg-zinc-800 transition-colors"
          >
            <i id="navIcon" class="fa-solid fa-bars text-xl"></i>
          </button>
        </div>
      </div>

      <!-- Mobile Dropdown -->
      <div
        id="mobileNavMenu"
        class="hidden lg:hidden bg-zinc-900 border-t border-zinc-800 shadow-xl"
        aria-hidden="true"
      >
        <div class="max-w-7xl mx-auto px-6 py-2">
          ${links.map(mobileLink).join('\n          ')}
        </div>
      </div>
    </nav>
  `;

  // Toggle function — exposed globally
  window.toggleMobileNav = function () {
    const menu = document.getElementById('mobileNavMenu');
    const icon = document.getElementById('navIcon');
    const btn  = document.getElementById('navToggleBtn');
    const isOpen = !menu.classList.contains('hidden');
    menu.classList.toggle('hidden', isOpen);
    menu.setAttribute('aria-hidden', String(isOpen));
    btn.setAttribute('aria-expanded', String(!isOpen));
    icon.className = isOpen ? 'fa-solid fa-bars text-xl' : 'fa-solid fa-xmark text-xl';
  };

  window.closeMobileNav = function () {
    const menu = document.getElementById('mobileNavMenu');
    const icon = document.getElementById('navIcon');
    const btn  = document.getElementById('navToggleBtn');
    if (menu) { menu.classList.add('hidden'); menu.setAttribute('aria-hidden', 'true'); }
    if (icon) icon.className = 'fa-solid fa-bars text-xl';
    if (btn)  btn.setAttribute('aria-expanded', 'false');
  };

  // Close on outside click
  document.addEventListener('click', function (e) {
    const menu = document.getElementById('mobileNavMenu');
    const btn  = document.getElementById('navToggleBtn');
    if (menu && btn && !menu.contains(e.target) && !btn.contains(e.target)) {
      if (!menu.classList.contains('hidden')) window.closeMobileNav();
    }
  });

  // Close on Escape key
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') window.closeMobileNav();
  });
})();
