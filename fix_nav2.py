import os
import re

files = [f for f in os.listdir('.') if f.endswith('.html')]

pages = {
    'index.html':      ('index.html',      'HOME',        'text-amber-400'),
    'about.html':      ('about.html',      'ABOUT US',    'text-amber-400'),
    'operations.html': ('operations.html', 'OPERATIONS',  'text-amber-400'),
    'gallery.html':    ('gallery.html',    'GALLERY',     'text-amber-400'),
    'locate.html':     ('locate.html',     'LOCATE US',   'text-amber-400'),
    'contact.html':    ('contact.html',    'CONTACT',     'text-amber-400'),
    'teams.html':      ('teams.html',      'TEAM',        'text-amber-400'),
}

def cls(f, link):
    return 'text-amber-400 font-semibold' if f == link else 'hover:text-amber-400 transition-colors'

for f in files:
    if f not in pages:
        continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()

    nav_block = f"""<!-- NAVIGATION -->
    <nav class="bg-zinc-950 border-b border-zinc-800 fixed w-full z-50">
        <div class="max-w-7xl mx-auto px-4 md:px-6">
            <div class="flex justify-between items-center h-20">
                <!-- Logo -->
                <a href="index.html" class="flex items-center gap-3 flex-shrink-0">
                    <img src="logo.jpeg" alt="Logo" class="h-10 w-auto">
                    <div>
                        <span class="text-base md:text-xl font-bold tracking-tighter">SAMMY SHARP</span>
                        <span class="block text-xs text-amber-400 -mt-1">OIL &amp; GAS LIMITED</span>
                    </div>
                </a>
                <!-- Desktop Links -->
                <div class="hidden lg:flex items-center gap-5 xl:gap-8 text-sm font-medium">
                    <a href="index.html" class="{cls(f, 'index.html')}">HOME</a>
                    <a href="about.html" class="{cls(f, 'about.html')}">ABOUT US</a>
                    <a href="operations.html" class="{cls(f, 'operations.html')}">OPERATIONS</a>
                    <a href="gallery.html" class="{cls(f, 'gallery.html')}">GALLERY</a>
                    <a href="locate.html" class="{cls(f, 'locate.html')}">LOCATE US</a>
                    <a href="contact.html" class="{cls(f, 'contact.html')}">CONTACT</a>
                    <a href="teams.html" class="{cls(f, 'teams.html')}">TEAM</a>
                </div>
                <!-- Hamburger -->
                <button onclick="toggleMobileMenu()" id="hamburgerBtn" aria-label="Open menu" class="lg:hidden text-white text-2xl p-2">
                    <i class="fa-solid fa-bars"></i>
                </button>
            </div>
        </div>
        <!-- Mobile Menu -->
        <div id="mobileMenu" class="hidden lg:hidden bg-zinc-900 border-t border-zinc-800">
            <div class="flex flex-col px-6 py-4">
                <a href="index.html" class="py-3 border-b border-zinc-800 {cls(f, 'index.html')}">HOME</a>
                <a href="about.html" class="py-3 border-b border-zinc-800 {cls(f, 'about.html')}">ABOUT US</a>
                <a href="operations.html" class="py-3 border-b border-zinc-800 {cls(f, 'operations.html')}">OPERATIONS</a>
                <a href="gallery.html" class="py-3 border-b border-zinc-800 {cls(f, 'gallery.html')}">GALLERY</a>
                <a href="locate.html" class="py-3 border-b border-zinc-800 {cls(f, 'locate.html')}">LOCATE US</a>
                <a href="contact.html" class="py-3 border-b border-zinc-800 {cls(f, 'contact.html')}">CONTACT</a>
                <a href="teams.html" class="py-3 {cls(f, 'teams.html')}">TEAM</a>
            </div>
        </div>
    </nav>"""

    new_content = re.sub(r'<!-- NAVIGATION -->.*?</nav>', nav_block, content, flags=re.DOTALL)

    with open(f, 'w', encoding='utf-8') as file:
        file.write(new_content)

print("All nav blocks updated successfully.")
