// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion
const lightCodeTheme = require('prism-react-renderer/themes/github');
const darkCodeTheme = require('prism-react-renderer/themes/dracula');

/** @type {import('@docusaurus/types').Config} */
module.exports = {
  title: 'CIRI Copilot',
  tagline: 'Contextual Intelligent Runtime Interface - Developer docs',
  url: 'https://adimis.in',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'Adimis',
  projectName: 'ciri',
  i18n: { defaultLocale: 'en', locales: ['en'] },
  markdown: {
    mermaid: true,
  },
  themes: ['@docusaurus/theme-mermaid'],
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl: 'https://github.com/adimis-ai/ciri/tree/main/docs-site/',
        },
        blog: false,
        theme: { customCss: require.resolve('./src/css/custom.css') },
      },
    ],
  ],
  themeConfig: {
    navbar: {
      title: 'CIRI',
      items: [
        { type: 'doc', docId: 'intro', position: 'left', label: 'Docs' },
        { href: 'https://github.com/adimis-ai/ciri', label: 'GitHub', position: 'right' },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        { title: 'Docs', items: [{ label: 'Getting Started', to: '/docs/getting-started' }] },
        { title: 'Community', items: [{ label: 'Contributing', to: '/docs/contributing' }] },
        { title: 'More', items: [{ label: 'GitHub', href: 'https://github.com/adimis-ai/ciri' }] },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Adimis.`,
    },
    prism: { theme: lightCodeTheme, darkTheme: darkCodeTheme },
  },
};
