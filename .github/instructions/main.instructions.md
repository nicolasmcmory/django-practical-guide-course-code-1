---
applyTo: "**"
---

# Project Coding Instructions

## Architecture

- Migrate from SOA toward **microservices** using the **Strangler Pattern**.
- Never import Django models directly across app boundaries. All cross-app data access goes through a `app/` layer.
- Relationships between apps use **ID-only** references (integers now; design for UUIDs/CharFields).
- Structure each Django app to be self-contained with its own `services/` layer for business logic.

## Tech Stack

- **AI**: Vertex AI and Gemini API via Google ADK.
- **Frontend**: HTMX, vanilla JS (Alpine.js where needed), Bootstrap + SASS, Django templates. DRF only for microservice APIs.
- **Databases**: PostgreSQL (primary RDBMS), Pinecone (vector DB).
- **DB Setup**: Primary-secondary replication (async/sync), query caching, PGbouncer for the monolith.

## Rendering & URL Strategy

- Default to **Server-Side Rendering (SSR)** with Django templates.
- Use **full page refreshes** for macro-interactions (navigation, form submissions).
- Use **HTMX partial swaps** for micro-interactions (inline updates, live search, toasts).
- Place all HTMX fragment endpoints in `partials.py`. Keep full-page views in `views.py`.
- Prefix all HTMX URLs with `/hx/`.

## Django Forms & Widget-Tweaks

- Keep `forms.py` clean: use `ModelForm` strictly as a data-validation engine with no styling or widget attributes — **Headless Intent**.
- Define all CSS classes, `hx-*` attributes, and `data-*` hooks exclusively in templates via `{% render_field %}`.
- Apply the **Atomic Partial** pattern: create `partials/field.html` for DOM structure and inject field-specific attributes with `{% render_field %}`.
- Never generate HTML attributes inside Python form classes. Only modify `.html` or `.css` for design changes.
-In Django views, avoid using specialized form-handling libraries or patterns. Stick to standard Django forms and views for maximum clarity and compatibility with HTMX (GET for form display, POST for submission, and partials for HTMX responses).

## Async Strategy

- **JavaScript**: always `async` — never block the UI thread.
- **Django/Python**: sync by default for DB queries, file I/O, and HTML rendering. Use `async` only for I/O-bound operations: 3rd-party APIs, email, WebSockets.

## Reliability

- Use **Compensating Transactions** instead of distributed transactions.
- Design all services to tolerate failure: automatic recovery, redundancy, and tested failovers.
- Apply client-side reliability patterns: Timeouts, Retries, Circuit Breaker.
- Apply server-side reliability patterns: Fail Fast, Shed Load, Back-pressure.
- CloudSQL standby: configure hot, warm, and cold standby.

## Deployment & Communication

- Deploy via **Kubernetes on Google Cloud Run**. Rolling updates for small features; A/B testing for large ones.
- Internal service communication: **gRPC**. Gateway/aggregation layer: **RESTful**.
- Async processing: **RabbitMQ** message queues.
- Serve static files via **GCS + Cloud CDN**: set `STATIC_URL` to the CDN URL and always reference assets with `{% static %}`.

## Security

- Never store secrets in code. Use **Google Secret Manager**.
- Disable dormant API keys. Enforce API restrictions and IAM Least Privilege via IAM Recommender.
- Enforce mandatory key rotation. Set Essential Contacts and configure Billing Anomaly/Budget Alerts.

## Performance

- **Network**: use persistent connections; compress payloads.
- **Memory**: keep code lean; prefer many small processes; compute derived data in business logic to avoid extra DB round-trips.
- **Disk I/O**: sequential logging, async I/O, separate static vs. dynamic cache layers, proper indexing.
- **CPU**: choose optimal data structures/algorithms; tune thread and connection pool sizes.
- **Locking**: keep non-locking work outside sync blocks; use lock splitting/striping; pessimistic locking for high contention, optimistic for low-to-moderate; prevent deadlocks by enforcing lock ordering.
- **Caching**: client-side via `localStorage` and HTMX; server-side for stateless operations. Maximize hit ratio by caching small, frequently accessed items.

## CSS / Frontend Standards

- Use **CSS Variables** for color palette (Primary, Secondary, Surface, Error), an 8px spacing scale, and fluid typography. Variables should be defined in a `:root` selector in the main stylesheet.
- Implement a **CSS Grid/Flexbox** layout system: Container, Holy Grail layout, Auto-fitting Cards.
- Always use **.css files** for styling. Never inline styles or generate them from Python.
- Include a browser-normalizing **Reset**.
- Ensure styles are compatible with HTMX request indicators (`.htmx-request`, `.htmx-indicator`).
- Keep stylesheet total size **under 10KB**.
- Use semantic HTML tags: `<section>`, `<main>`, `<article>`, `<nav>`, `<header>`, `<footer>`.

## Code Quality

- Place a **Rational Block** comment at the top of every file describing its purpose, responsibilities, and key decisions. This provides immediate context for AI coding assistants and human reviewers.
- Write unit tests with the **Django test framework**. Write UI tests (including HTMX and JS behavior) with **Selenium**.

