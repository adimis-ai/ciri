import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';

export default function Home() {
  return (
    <Layout title="CIRI Copilot" description="CIRI: The Autonomous, Self-Evolving AI Copilot">
      <header className="hero-banner">
        <div className="container">
          <h1 className="hero-title">CIRI Copilot</h1>
          <p className="hero-subtitle">
            CIRI is an autonomous, self-evolving AI copilot that lives inside your workspace.
            It combines deep filesystem integration with multi-agent orchestration to permanently expand its own capabilities.
          </p>
          <div style={{ display: 'flex', gap: '1rem', justifyContent: 'center' }}>
            <Link className="button-primary" to="/docs/intro">
              Get Started
            </Link>
            <Link className="button-primary" style={{ background: 'transparent', border: '1px solid var(--ifm-color-primary)' }} to="/docs/architecture/overview">
              Core Concepts
            </Link>
          </div>
        </div>
      </header>

      <main>
        <div className="feature-grid">
          <div className="feature-card">
            <h3>Self-Evolution</h3>
            <p>Permanently expands its own abilities by creating new Skills, Toolkits, and SubAgents as it learns about your environment.</p>
          </div>
          <div className="feature-card">
            <h3>Workspace-Aware</h3>
            <p>Deeply integrated with your local files, history, and domain context for highly accurate reasoning and automation.</p>
          </div>
          <div className="feature-card">
            <h3>Web Research</h3>
            <p>Uses your real browser via CDP to perform deep research across internal docs, AWS consoles, and external APIs.</p>
          </div>
          <div className="feature-card">
            <h3>Multi-Agent</h3>
            <p>Delegates complex tasks to specialized builders and researchers, ensuring high performance across diverse domains.</p>
          </div>
          <div className="feature-card">
            <h3>Local-First</h3>
            <p>Operates inside your workspace with privacy in mind. Message history and checkpoints are stored locally in SQLite.</p>
          </div>
          <div className="feature-card">
            <h3>Extensible MCP</h3>
            <p>Native support for the Model Context Protocol, allowing seamless integration with any standard MCP toolkits.</p>
          </div>
        </div>

        <section style={{ padding: '4rem 2rem', textAlign: 'center', background: 'rgba(255, 255, 255, 0.02)' }}>
          <h2>Ready to evolve your workspace?</h2>
          <p style={{ marginBottom: '2rem', opacity: 0.7 }}>Install CIRI today and start building the future of autonomous development.</p>
          <Link className="button-primary" to="/docs/getting-started">
            Install Now
          </Link>
        </section>
      </main>
    </Layout>
  );
}
