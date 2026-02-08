---
title: "Soutenir I2P"
slug: "financial-support"
layout: single
aliases: 
---

<style>   /* Override single.html layout constraints */   .single-page .page-header {

    display: none;
}   .single-page .page-content {

    max-width: none;
}   .single-page {

    padding-top: 0;
}

.support-container {

    margin: 0 auto;
}

/* ── Mise en page à deux colonnes avec table des matières ── */   .support-layout {

    display: grid;
    grid-template-columns: 260px 1fr;
    gap: var(--spacing-2xl);
    align-items: start;
}

.support-main {

    min-width: 0;
}

.support-toc {

    position: sticky;
    top: 100px;
    max-height: calc(100vh - 120px);
    overflow-y: auto;
}

.support-toc nav {

    background: var(--color-bg-secondary);
    border: 1px solid var(--color-border);
    border-radius: 10px;
    padding: 1rem;
}

.support-toc .toc-title {

    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-weight: 700;
    font-size: 0.8125rem;
    color: var(--color-text);
    padding-bottom: 0.75rem;
    margin-bottom: 0.75rem;
    border-bottom: 1px solid var(--color-border);
    text-transform: uppercase;
    letter-spacing: 0.04em;
}

.support-toc ul {

    list-style: none;
    padding: 0;
    margin: 0;
}

.support-toc li {

    margin-bottom: 0.2rem;
}

.support-toc a {

    display: block;
    padding: 0.3rem 0.6rem;
    font-size: 0.8125rem;
    color: var(--color-text-secondary);
    text-decoration: none;
    border-radius: 4px;
    transition: all 0.15s ease;
    line-height: 1.4;
}

.support-toc a:hover {

    color: var(--color-primary);
    background: var(--color-bg-tertiary);
}

@media (max-width: 1024px) {

    .support-layout {
      grid-template-columns: 1fr;
    }
    .support-toc {
      display: none;
    }
}

/* ── Animated Hero ── */   .support-hero {

    padding: 3rem 2rem;
    border: 1px solid var(--color-border);
    border-radius: 12px;
    background: linear-gradient(-45deg, var(--color-bg-secondary), var(--color-bg), rgba(30,64,175,0.06), rgba(124,58,237,0.06));
    background-size: 400% 400%;
    animation: heroShift 15s ease infinite;
    margin-bottom: 3rem;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    text-align: center;
}

@keyframes heroShift {

    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.support-hero h1 {

    margin-top: 0;
    margin-bottom: 1rem;
    font-size: 2.5rem;
    background: linear-gradient(135deg, var(--color-primary) 0%, #7c3aed 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.support-hero p {

    font-size: 1.125rem;
    line-height: 1.7;
    max-width: 750px;
    margin: 0 auto;
    color: var(--color-text-secondary);
}

/* ── Styles de section avec arrière-plans alternés ── */   .support-section {

    margin-bottom: 0;
    padding: 3rem 0;
}

.support-section:first-child {

    padding-top: 0;
}

.support-section:nth-child(even) {

    background: var(--color-bg-secondary);
    margin-left: -2rem;
    margin-right: -2rem;
    padding-left: 2rem;
    padding-right: 2rem;
    border-radius: 12px;
}

.page-content .support-section h2 {

    display: flex;
    align-items: center;
    gap: 0.75rem;
    margin: 0 0 1rem 0;
    font-size: 1.875rem;
    color: var(--color-text);
    scroll-margin-top: 100px;
}

.support-section h2 .section-icon {

    flex-shrink: 0;
    color: var(--color-primary);
}

.support-section > p {

    color: var(--color-text-secondary);
    line-height: 1.7;
    margin-bottom: 1.5rem;
}

/* ── Card grid ── */   .support-grid {

    display: grid;
    gap: 1rem;
    margin: 1rem 0 1.5rem 0;
}

@media (min-width: 768px) {

    .support-grid {
      grid-template-columns: repeat(2, 1fr);
    }
}

.support-card {

    border: 1px solid var(--color-border);
    border-radius: 8px;
    padding: 0.75rem 1rem;
    background: var(--color-bg);
    transition: all 0.2s ease;
    display: flex;
    flex-direction: column;
}

.support-card:hover {

    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    border-color: var(--color-primary);
}

.page-content .support-card h3 {

    margin: 0 0 0.35rem 0;
    padding: 0;
    color: var(--color-primary);
    font-size: 1rem;
}

.page-content .support-card p {

    margin: 0 0 0.25rem 0;
    line-height: 1.5;
    font-size: 0.9rem;
    color: var(--color-text-secondary);
}

/* ── Liste avec coches ── */   .support-list {

    margin: 0;
    padding: 0;
    list-style: none;
}

.support-list li {

    margin-bottom: 0.15rem;
    padding-left: 1.25rem;
    position: relative;
    line-height: 1.4;
    font-size: 0.875rem;
}

.support-list li:last-child {

    margin-bottom: 0;
}

.support-list li::before {

    content: "✓";
    position: absolute;
    left: 0;
    color: var(--color-primary);
    font-weight: bold;
    font-size: 0.95rem;
}

/* ── Cartes de don crypto ── */   .donation-methods {

    display: grid;
    gap: 1rem;
    margin-top: 1rem;
}

.donation-method {

    border: 1px solid var(--color-border);
    border-radius: 8px;
    padding: 1rem 1.25rem;
    background: var(--color-bg);
    transition: border-color 0.2s ease;
}

.donation-method:hover {

    border-color: var(--color-primary);
}

.donation-method h4 img.crypto-logo {

    width: 24px;
    height: 24px;
    vertical-align: middle;
    margin-right: 0.35rem;
    position: relative;
    top: -1px;
}

.donation-method .crypto-info {

    min-width: 0;
}

.page-content .donation-method h4 {

    margin: 0 0 0.4rem 0;
    font-size: 1.125rem;
    color: var(--color-text);
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.page-content .donation-method p {

    margin: 0 0 0.5rem 0;
}

.donation-method h4 .badge {

    font-size: 0.7rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    padding: 0.15rem 0.5rem;
    border-radius: 20px;
    background: rgba(30, 64, 175, 0.1);
    color: var(--color-primary);
}

.page-content .donation-method p {

    color: var(--color-text-secondary);
    font-size: 0.9rem;
    line-height: 1.5;
}

.crypto-address {

    font-family: 'Monaco', 'Menlo', 'Courier New', monospace;
    font-size: 0.8125rem;
    padding: 0.5rem 0.75rem;
    background: var(--color-bg-secondary);
    border: 1px solid var(--color-border);
    border-radius: 6px;
    word-break: break-all;
    color: var(--color-primary);
    user-select: all;
    cursor: pointer;
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
}

.crypto-address:hover {

    border-color: var(--color-primary);
    box-shadow: 0 0 0 2px rgba(30, 64, 175, 0.1);
}

.select-hint {

    font-size: 0.75rem;
    color: var(--color-text-muted);
    margin-top: 0.35rem;
    display: block;
}

@media (max-width: 600px) {

    .donation-method {
      flex-direction: row;
    }
}

/* ── Cartes de niveaux de parrainage ── */   .tier-grid {

    display: grid;
    gap: 1.5rem;
    margin: 1.5rem 0;
}

@media (min-width: 768px) {

    .tier-grid {
      grid-template-columns: repeat(3, 1fr);
    }
}

.tier-card {

    border: 1px solid var(--color-border);
    border-radius: 8px;
    overflow: hidden;
    background: var(--color-bg);
    transition: all 0.2s ease;
    text-align: center;
    padding-bottom: 1.5rem;
}

.tier-card:hover {

    transform: translateY(-2px);
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
}

.tier-card .tier-header {

    padding: 1.25rem 1.5rem;
    color: #fff;
}

.tier-card .tier-header h4 {

    margin: 0;
    font-size: 1.25rem;
    color: inherit;
}

.tier-card .tier-header .tier-price {

    font-size: 0.9rem;
    opacity: 0.9;
    margin-top: 0.25rem;
}

.tier-card .tier-body {

    padding: 1.25rem 1.5rem 0;
}

.tier-card .tier-body p {

    margin: 0;
    color: var(--color-text-secondary);
    line-height: 1.6;
    font-size: 0.95rem;
}

.tier-bronze .tier-header { background: linear-gradient(135deg, #92400e, #b45309); }   .tier-silver .tier-header { background: linear-gradient(135deg, #475569, #64748b); }   .tier-gold   .tier-header { background: linear-gradient(135deg, #92400e, #ca8a04); }

.tier-bronze:hover { border-color: #b45309; }   .tier-silver:hover { border-color: #64748b; }   .tier-gold:hover   { border-color: #ca8a04; }

/* ── Boîte d'information ── */   .info-box {

    border-radius: 8px;
    border: 1px solid var(--color-border);
    padding: 1.25rem 1.5rem;
    background: var(--color-bg-secondary);
    margin: 1.5rem 0;
    line-height: 1.6;
}

.info-box strong {

    color: var(--color-primary);
}

.info-box p {

    margin: 0;
}

/* ── Bientôt disponible ── */   .coming-soon {

    border-radius: 8px;
    border: 2px dashed var(--color-border);
    padding: 2.5rem 2rem;
    background: rgba(30, 64, 175, 0.03);
    text-align: center;
    color: var(--color-text-secondary);
}

.coming-soon .coming-soon-icon {

    display: block;
    margin: 0 auto 0.75rem;
    color: var(--color-text-muted);
}

.coming-soon p {

    margin: 0;
    font-weight: 500;
}

/* ── Liens de carte CTA ── */   .support-card .card-cta {

    margin-top: auto;
    padding-top: 1rem;
}

.support-card .card-cta a {

    display: inline-block;
    padding: 0.4rem 1.15rem;
    border: 1.5px solid var(--color-primary);
    border-radius: 20px;
    color: var(--color-primary);
    text-decoration: none;
    font-size: 0.875rem;
    font-weight: 500;
    transition: all 0.2s ease;
}

.support-card .card-cta a:hover {

    background: var(--color-primary);
    color: #fff;
}

/* ── Mise en avant des fonctionnalités ── */   .feature-highlight {

    background: var(--color-bg-secondary);
    border-left: 4px solid var(--color-primary);
    padding: 1.25rem 1.5rem;
    margin: 1.5rem 0;
    border-radius: 4px;
}

.feature-highlight p {

    margin: 0;
    line-height: 1.6;
} </style>

<div class="support-container">
<div class="support-layout">

<aside class="support-toc">
  <nav>
    <div class="toc-title">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 6h16M4 12h16M4 18h16"/></svg>
      On This Page
    </div>
    <ul>
      <li><a href="#donate">Donate to I2P</a></li>
      <li><a href="#why-support">Why Your Support Matters</a></li>
      <li><a href="#sponsor">Sponsor Development</a></li>
      <li><a href="#corporate">Corporate Support</a></li>
      <li><a href="#transparency">Financial Transparency</a></li>
      <li><a href="#other-ways">Other Ways to Help</a></li>
    </ul>
  </nav>
</aside>

<div class="support-main">

<div class="support-section">
  <h2 id="donate">
    <svg class="section-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/></svg>
    Donate to I2P
  </h2>
  <p>Your contribution keeps the I2P network resilient, censorship-resistant, and accessible to everyone. We accept multiple donation methods to respect your privacy preferences.</p>

  <a href="#XLLURLEG" style="display: none"></a>

  <!-- FundraiseUp Standard Snippet - loads only on this page -->
  <script>(function(w,d,s,n,a){if(!w[n]){var l='call,catch,on,once,set,then,track'
  .split(','),i,o=function(n){return'function'==typeof n?o.l.push([arguments])&&o
  :function(){return o.l.push([n,arguments])&&o}},t=d.getElementsByTagName(s)[0],
  j=d.createElement(s);j.async=!0;j.src='https://cdn.fundraiseup.com/widget/'+a;
  t.parentNode.insertBefore(j,t);o.s=Date.now();o.v=4;o.h=w.location.href;o.l=[];
  for(i=0;i<7;i++)o[l[i]]=o(l[i]);w[n]=o}
  })(window,document,'script','FundraiseUp','AAYKECHT');</script>

  <div class="donation-methods">
    <div class="donation-method">
      <div class="crypto-info">
        <h4><img class="crypto-logo" src="/images/monero-xmr-logo.svg" alt="Monero" /> Monero (XMR) <span class="badge">Recommended</span></h4>
        <p>Monero provides the strongest privacy guarantees for donations. All transactions are confidential and untraceable.</p>
        <div class="crypto-address">85igd4Dw6ychvi8iUYADHfgLCmdT348SA6sMnYgxE86YZxX98Au6rsF9B9DmcqEXWRZWDcPdarufHUUqwP73GVrq6BaC9dr</div>
        <span class="select-hint">Click address to select</span>
      </div>
    </div>
    <div class="donation-method">
      <div class="crypto-info">
        <h4><img class="crypto-logo" src="/images/bitcoin-btc-logo.svg" alt="Bitcoin" /> Bitcoin (BTC)</h4>
        <p>Bitcoin donations are accepted for convenience, though they offer less privacy than Monero.</p>
        <div class="crypto-address">3JSSF45pAW5ujWbBuRFe25pBiwp1vjSRNb</div>
        <span class="select-hint">Click address to select</span>
      </div>
    </div>
    <div class="donation-method">
      <div class="crypto-info">
        <h4><img class="crypto-logo" src="/images/zcash-zec-logo.svg" alt="Zcash" /> Zcash (ZEC)</h4>
        <p>Zcash offers enhanced privacy features for those who prefer this cryptocurrency.</p>
        <div class="crypto-address">t1TwTuu4qU25aGvh59EMkCAZdmwJepkyQcD</div>
        <span class="select-hint">Click address to select</span>
      </div>
    </div>
  </div>

  <div class="info-box">
    <p><strong>Privacy First:</strong> We recommend cryptocurrency donations for maximum anonymity. All donations support the entire project.</p>
    <p style="margin-top: 0.75rem;"><strong>Other Cryptocurrencies:</strong> Want to donate using a different cryptocurrency? Please <a href="/en/contact/">contact us</a> and we'll provide an address for your preferred currency.</p>
  </div>
</div>


<div class="support-section">
  <h2 id="why-support">
    <svg class="section-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
    Why Your Support Matters
  </h2>
  <p>I2P is built and maintained entirely by volunteers. Donations enable critical infrastructure and development work that keeps the network running.</p>

  <div class="support-grid">
    <div class="support-card">
      <h3>Infrastructure & Operations</h3>
      <ul class="support-list">
        <li>Maintain reseed servers worldwide</li>
        <li>Run build systems, mirrors, and hosting</li>
        <li>Pay for bandwidth and server costs</li>
        <li>Renew domains and SSL certificates</li>
      </ul>
    </div>
    <div class="support-card">
      <h3>Security & Research</h3>
      <ul class="support-list">
        <li>Commission independent security audits</li>
        <li>Implement post-quantum cryptography</li>
        <li>Research new privacy techniques</li>
        <li>Partner with universities on research</li>
      </ul>
    </div>
    <div class="support-card">
      <h3>Development</h3>
      <ul class="support-list">
        <li>Implement new protocol features</li>
        <li>Fix critical bugs and improve performance</li>
        <li>Prototype performance improvements</li>
        <li>Build better user experiences</li>
      </ul>
    </div>
    <div class="support-card">
      <h3>Community</h3>
      <ul class="support-list">
        <li>Translate documentation into new languages</li>
        <li>Support new contributors and mentoring</li>
        <li>Fund travel to developer summits</li>
        <li>Expand presence at privacy conferences</li>
      </ul>
    </div>
  </div>
</div>


<div class="support-section">
  <h2 id="sponsor">
    <svg class="section-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"/><path d="m12 15-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/><path d="M9 12H4s.55-3.03 2-4c1.62-1.08 5 0 5 0"/><path d="M12 15v5s3.03-.55 4-2c1.08-1.62 0-5 0-5"/></svg>
    Sponsor Specific Development
  </h2>
  <div class="coming-soon">
    <svg class="coming-soon-icon" xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>
    <p>Coming soon &mdash; Community Crowdfunding System for targeted development projects</p>
  </div>
</div>


<div class="support-section">
  <h2 id="corporate">
    <svg class="section-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 22V4a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v18Z"/><path d="M6 12H4a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h2"/><path d="M18 9h2a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2h-2"/><path d="M10 6h4"/><path d="M10 10h4"/><path d="M10 14h4"/><path d="M10 18h4"/></svg>
    Corporate & Institutional Support
  </h2>
  <p>Companies and organizations that benefit from I2P can support the project through corporate sponsorship. Sponsors can fund general operations, specific research initiatives, or community programs.</p>

  <div class="tier-grid">
    <div class="tier-card tier-bronze">
      <div class="tier-header">
        <h4>Bronze</h4>
        <div class="tier-price">$1,000+</div>
      </div>
      <div class="tier-body">
        <p>Logo featured on the I2P website with a link to your organization.</p>
      </div>
    </div>
    <div class="tier-card tier-silver">
      <div class="tier-header">
        <h4>Silver</h4>
        <div class="tier-price">$5,000+</div>
      </div>
      <div class="tier-body">
        <p>Logo on website plus mention in official release notes and announcements.</p>
      </div>
    </div>
    <div class="tier-card tier-gold">
      <div class="tier-header">
        <h4>Gold</h4>
        <div class="tier-price">$10,000+</div>
      </div>
      <div class="tier-body">
        <p>Logo on website, release note mentions, and priority support for technical questions.</p>
      </div>
    </div>
  </div>

  <div class="info-box">
    <p>All corporate sponsors are reviewed to ensure alignment with I2P's privacy mission. Contact <strong>admin@i2p.net</strong> to discuss sponsorship opportunities.</p>
  </div>
</div>


<div class="support-section">
  <h2 id="transparency">
    <svg class="section-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>
    Financial Transparency
  </h2>
  <div class="info-box">
    <p>
      <strong>Coming 2026:</strong> Formal financial statements and annual reports will be published starting in 2026. We're committed to full transparency about how community funds are used.
    </p>
  </div>
</div>


<div class="support-section">
  <h2 id="other-ways">
    <svg class="section-icon" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
    Other Ways to Help
  </h2>
  <p>Don't have funds to donate? There are many other valuable ways to support I2P:</p>

  <div class="support-grid">
    <div class="support-card">
      <h3>Contribute Code</h3>
      <p>Help develop I2P by contributing to the Java router, Android app, or supporting tools. Check our GitLab for open issues.</p>
      <div class="card-cta">
        <a href="/en/docs/development/applications/">Get started →</a>
      </div>
    </div>
    <div class="support-card">
      <h3>Run Infrastructure</h3>
      <p>Operate a reseed server, build system, or mirror to help strengthen the network's infrastructure.</p>
      <div class="card-cta">
        <a href="/en/docs/guides/mirroring-guide/">Mirroring guide →</a>
      </div>
    </div>
    <div class="support-card">
      <h3>Improve Documentation</h3>
      <p>Write guides, translate docs, or help new users get started with I2P on forums and support channels.</p>
      <div class="card-cta">
        <a href="/en/get-involved/">Learn more →</a>
      </div>
    </div>
    <div class="support-card">
      <h3>Spread Awareness</h3>
      <p>Tell others about I2P, write blog posts, give talks, or share information about privacy technology.</p>
      <div class="card-cta">
        <a href="/en/blog/">Read our blog →</a>
      </div>
    </div>
  </div>
</div>

<div class="info-box" style="text-align: center; margin-top: 3rem;">
  <p><strong>Thank you for supporting internet privacy and freedom!</strong></p>
  <p style="margin-top: 0.5rem;">Every contribution, large or small, helps keep I2P strong and independent.</p>
</div>

</div><!-- /.support-main -->
</div><!-- /.support-layout -->
</div><!-- /.support-container -->