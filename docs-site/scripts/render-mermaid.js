const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const docsDir = path.join(__dirname, '..', 'docs');
const outDir = path.join(__dirname, '..', 'static', 'img', 'mermaid');

function ensureDir(dir) {
  if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
}

function findMermaidBlocks(file) {
  const content = fs.readFileSync(file, 'utf8');
  const regex = /```mermaid\n([\s\S]*?)```/g;
  let m;
  const blocks = [];
  while ((m = regex.exec(content)) !== null) {
    blocks.push(m[1]);
  }
  return blocks;
}

function walk(dir) {
  const files = [];
  for (const name of fs.readdirSync(dir)) {
    const full = path.join(dir, name);
    if (fs.statSync(full).isDirectory()) {
      files.push(...walk(full));
    } else if (full.endsWith('.md')) {
      files.push(full);
    }
  }
  return files;
}

ensureDir(outDir);

const files = walk(docsDir);
let count = 0;
for (const file of files) {
  const blocks = findMermaidBlocks(file);
  blocks.forEach((block, idx) => {
    const outFile = path.join(outDir, path.basename(file).replace(/\.md$/, '') + '-' + idx + '.svg');
    try {
      // Use mermaid-cli to render to SVG
      const tmpFile = outFile + '.mmd';
      fs.writeFileSync(tmpFile, block);
      // Prefer local node_modules .bin/mmdc if available, else fall back to npx
      const localMmdc = path.join(__dirname, '..', 'node_modules', '.bin', process.platform === 'win32' ? 'mmdc.cmd' : 'mmdc');
      const cmd = fs.existsSync(localMmdc)
        ? `"${localMmdc}" -i "${tmpFile}" -o "${outFile}" --width 800 --height 600`
        : `npx -y @mermaid-js/mermaid-cli -i "${tmpFile}" -o "${outFile}" --width 800 --height 600`;
      execSync(cmd, { stdio: 'ignore' });
      fs.unlinkSync(tmpFile);
      console.log(`Rendered ${outFile}`);
      count++;
    } catch (e) {
      console.error('Failed to render mermaid for', file, e.message);
    }
  });
}
console.log(`Rendered ${count} mermaid diagrams.`);
