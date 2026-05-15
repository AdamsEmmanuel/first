# AI Frontend MVP Generation Template

## Purpose

Use this template whenever generating frontend applications with AI tools like [Claude AI](https://claude.ai?utm_source=chatgpt.com) or [ChatGPT](https://chatgpt.com?utm_source=chatgpt.com).

The goal is to consistently generate:

* scalable
* maintainable
* deployable
* production-ready
* responsive
* backend-friendly
  frontend MVPs.

---

# MASTER AI PROMPT TEMPLATE

```txt
Build a production-ready frontend MVP application.

Tech Stack:
- React + TypeScript
- Vite
- TailwindCSS
- shadcn/ui
- Zustand for state management
- TanStack Query for server state
- React Hook Form + Zod for forms and validation

Requirements:
- scalable architecture
- feature-based folder structure
- reusable components
- responsive mobile-first design
- centralized API layer
- environment variable support
- loading and error states
- protected routes
- JWT authentication flow
- proper form validation
- accessibility support
- lazy loading
- route-based code splitting
- deployment-ready configuration
- clean maintainable code
- separation of concerns

Backend Assumptions:
- FastAPI backend
- JWT auth
- REST APIs
- paginated endpoints
- proper HTTP status handling

Deployment Targets:
- Vercel frontend
- Docker support

Important:
- Do not place all logic in App.tsx
- Separate UI, business logic, and API logic
- Use reusable components
- Avoid duplicated code
- Never hardcode localhost URLs
- Use environment variables
- Include loading, empty, and error states
- Add retry handling for failed requests
- Include accessibility improvements
- Add comments explaining architecture decisions
```

---

# PROJECT GENERATION WORKFLOW

## STEP 1 — Generate Architecture

```txt
Design the architecture for a scalable frontend MVP.
Explain:
- architecture decisions
- scaling considerations
- tradeoffs
- future improvements
```

---

## STEP 2 — Generate Folder Structure

```txt
Generate a scalable feature-based folder structure.
Separate:
- components
- pages
- services
- hooks
- routes
- store
- layouts
- utilities
- API layer
- feature modules
```

Expected Structure:

```txt
src/
 ├── api/
 ├── assets/
 ├── components/
 ├── features/
 ├── hooks/
 ├── layouts/
 ├── pages/
 ├── routes/
 ├── services/
 ├── store/
 ├── styles/
 ├── types/
 ├── utils/
 └── App.tsx
```

---

## STEP 3 — Generate Core Systems

### Authentication

```txt
Implement a real JWT authentication flow:
- login
- logout
- auth persistence
- protected routes
- refresh tokens
- token expiration handling
```

### API Layer

```txt
Create:
- centralized API client
- axios instance
- token interceptors
- request timeout handling
- retry handling
- API error normalization
```

### State Management

```txt
Use Zustand for global state.
Keep server state separate from UI state.
Use TanStack Query for server caching.
```

---

## STEP 4 — Generate Reusable Components

```txt
Create reusable components for:
- buttons
- cards
- tables
- loaders
- forms
- alerts
- modals
- pagination
- dropdowns
- navigation
```

Component Rules:

```txt
All components must:
- accept props
- support loading states
- support disabled states
- support accessibility
- be reusable
- avoid duplicated logic
```

---

## STEP 5 — Generate Feature Modules Incrementally

Example:

```txt
Generate the dashboard feature module only.
Include:
- pages
- API integration
- components
- loading states
- error states
- responsive layout
```

Do NOT generate the entire application in one step.

---

# FRONTEND ENGINEERING RULES

## 1. Separation of Concerns

Never:

* fetch data directly inside UI components
* place all logic inside App.tsx
* mix API calls with presentation logic
* duplicate business logic

Instead:

* services handle API logic
* hooks manage state logic
* components handle presentation
* stores manage global state

---

# 2. API Standards

Always:

* use environment variables
* centralize API calls
* normalize API errors
* handle loading states
* handle retry logic
* handle empty states
* support pagination

Example:

```env
VITE_API_BASE_URL=https://api.example.com
```

---

# 3. Authentication Rules

Always:

* protect authenticated routes
* persist auth state
* handle expired tokens
* use interceptors for auth headers
* support logout properly

Never:

* hardcode tokens
* expose secrets
* store sensitive credentials insecurely

---

# 4. Responsive Design Rules

Always:

* design mobile-first
* support tablets and desktop
* use responsive Tailwind utilities
* avoid fixed widths
* test different screen sizes

Target Breakpoints:

* 320px mobile
* tablet
* laptop
* ultrawide desktop

---

# 5. Form Standards

Always use:

* React Hook Form
* Zod validation
* reusable form inputs
* inline validation messages

Each form should support:

* loading state
* success state
* error handling
* disabled submit during requests

---

# 6. UX Standards

Every async UI should include:

* loading skeletons
* retry buttons
* empty states
* success feedback
* error feedback

Never leave blank screens.

---

# 7. Performance Standards

Always optimize:

* lazy loading
* route splitting
* minimized rerenders
* image optimization
* caching

Use:

* React.lazy
* Suspense
* memoization when necessary
* TanStack Query caching

---

# 8. Accessibility Standards

Always include:

* semantic HTML
* aria labels
* keyboard navigation
* visible focus states
* accessible forms
* sufficient contrast

---

# 9. Deployment Readiness

The app must:

* build successfully
* support production environment variables
* avoid localhost dependencies
* support Docker deployment
* support Vercel deployment

---

# 10. Error Handling

Always implement:

* React error boundaries
* API error normalization
* fallback UI
* retry handling
* graceful failures

---

# RECOMMENDED STACK

## Fast MVP Stack

```txt
- React
- Vite
- TailwindCSS
- shadcn/ui
- Zustand
- TanStack Query
- React Hook Form
- Zod
```

---

# BACKEND INTEGRATION GUIDELINES

Assume backend APIs:

```txt
- FastAPI
- JWT auth
- RESTful endpoints
- pagination
- filtering
- file uploads
- proper HTTP status codes
```

Frontend should support:

* token refresh
* pagination
* filtering
* search
* optimistic updates
* retries

---

# AI PROMPTING BEST PRACTICES

## DO

* generate features incrementally
* ask for architecture explanations
* request reusable components
* request deployment readiness
* request accessibility support
* request TypeScript typing
* request error handling

## DO NOT

* generate entire apps in one prompt
* allow all logic in one file
* hardcode API URLs
* skip loading/error states
* skip responsiveness
* skip accessibility

---

# PRODUCTION CHECKLIST

Before deployment verify:

## Architecture

* [ ] scalable folder structure
* [ ] reusable components
* [ ] centralized API layer
* [ ] proper state management

## UX

* [ ] loading states
* [ ] error states
* [ ] empty states
* [ ] responsive design

## Security

* [ ] protected routes
* [ ] token handling
* [ ] environment variables
* [ ] no secrets exposed

## Performance

* [ ] lazy loading
* [ ] route splitting
* [ ] optimized assets
* [ ] minimized rerenders

## Deployment

* [ ] production build works
* [ ] environment variables configured
* [ ] API URLs configured
* [ ] Docker/Vercel ready

---

# RECOMMENDED TOOLS

## Frontend

* React
* TypeScript
* TailwindCSS
* shadcn/ui
* Zustand
* TanStack Query
* Framer Motion
* React Hook Form
* Zod

## Backend

* FastAPI
* PostgreSQL
* Redis
* Celery
* Docker

## Deployment

* [Vercel](https://vercel.com?utm_source=chatgpt.com)
* [Render](https://render.com?utm_source=chatgpt.com)
* [Fly.io](https://fly.io?utm_source=chatgpt.com)
* [Hetzner](https://www.hetzner.com?utm_source=chatgpt.com)
* [Railway](https://railway.app?utm_source=chatgpt.com)

---

# FINAL PRINCIPLE

The goal of AI-generated frontend development is NOT just:

> “make the UI look good.”

The real goal is:

* maintainability
* scalability
* clean architecture
* backend compatibility
* deployment readiness
* fast iteration speed

Think like a software engineer first.

Use AI as an accelerator, not as a replacement for engineering judgment.
