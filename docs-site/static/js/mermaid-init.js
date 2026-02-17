document.addEventListener('DOMContentLoaded', function () {
  try {
    if (typeof mermaid === 'undefined') {
      console.warn('mermaid not loaded');
      return;
    }
    // Initialize mermaid without auto start
    mermaid.initialize({ startOnLoad: false });

    // Replace fenced mermaid code blocks (<pre><code class="language-mermaid">) with <div class="mermaid">..</div>
    const codeBlocks = Array.from(document.querySelectorAll('pre > code.language-mermaid'));
    codeBlocks.forEach((code) => {
      const pre = code.parentElement;
      const wrapper = document.createElement('div');
      wrapper.className = 'mermaid';
      // Use textContent to preserve the raw mermaid syntax
      wrapper.textContent = code.textContent;
      // Replace the <pre> element with the mermaid div
      pre.parentElement.replaceChild(wrapper, pre);
    });

    // Also handle <code class="language-mermaid"> not wrapped in pre
    const inlineBlocks = Array.from(document.querySelectorAll('code.language-mermaid'));
    inlineBlocks.forEach((code) => {
      const wrapper = document.createElement('div');
      wrapper.className = 'mermaid';
      wrapper.textContent = code.textContent;
      code.parentElement.replaceChild(wrapper, code);
    });

    // Initialize rendering on all mermaid divs
    const mermaidDivs = document.querySelectorAll('.mermaid');
    if (mermaidDivs.length > 0) {
      try {
        mermaid.init(undefined, mermaidDivs);
      } catch (err) {
        // Fallback: use promise-based render if init fails
        Array.from(mermaidDivs).forEach((el, idx) => {
          const code = el.textContent || '';
          const id = 'mermaid-' + idx + '-' + Math.random().toString(36).slice(2, 10);
          // mermaid.render may be async returning an SVG string
          try {
            const rendered = mermaid.render(id, code);
            // If render returns a string, replace innerHTML
            if (typeof rendered === 'string') {
              el.innerHTML = rendered;
            }
          } catch (e) {
            // ignore per-element failures
            console.warn('mermaid render failed for element', e);
          }
        });
      }
    }
  } catch (e) {
    console.error('Error initializing mermaid rendering:', e);
  }
});
