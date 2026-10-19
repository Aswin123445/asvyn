# Deployment and Debugging

## Overview

This section documents my experience deploying backend applications, configuring servers, managing application processes, and troubleshooting deployment issues.

My experience includes working with Django, FastAPI, Gunicorn, Nginx, Docker, Redis, Celery, PostgreSQL, GitHub Actions, and AWS EC2.

The documentation distinguishes between configurations I have implemented, problems I have encountered, and techniques I am still learning.

## Deployment Technologies

### AWS EC2

- Hosting backend applications on an EC2 instance running Ubuntu.
- Connecting to remote servers using SSH.
- Configuring application environments and deployment dependencies.
- Managing application processes and server resources.

### Gunicorn

- Running Django applications through Gunicorn.
- Understanding the relationship between the WSGI application and the application server.
- Investigating application startup failures and Python import errors.

### Nginx

- Configuring Nginx as a reverse proxy.
- Forwarding incoming HTTP requests to the application server.
- Investigating HTTP 502 Bad Gateway errors.
- Troubleshooting static-file access and permission issues.

### Docker and Docker Compose

- Containerizing application services.
- Configuring services such as PostgreSQL and Redis.
- Managing environment variables and service configuration.
- Investigating container startup and service connectivity issues.

### GitHub Actions

- Working with automated build and deployment workflows.
- Troubleshooting workflow failures related to project paths, PostgreSQL services, and dependency installation.

## Debugging Experiences

### 1. Nginx 502 Bad Gateway

**Problem:** An Nginx server can return a 502 response when it cannot obtain a valid response from the upstream application server.

**Investigation areas:**
- Check whether Gunicorn or the relevant application process is running.
- Inspect application-server logs.
- Verify the upstream host, port, or Unix socket.
- Check service connectivity and startup errors.

**Personal incident:** Add the specific project, observed error, confirmed cause, fix, and outcome.

### 2. Gunicorn Module Import Errors

**Problem:** An application may fail to start if Gunicorn cannot import the configured Python module or application object.

**Investigation areas:**
- Verify the working directory.
- Check the Python module path and WSGI application reference.
- Confirm the virtual environment and installed dependencies.
- Inspect the full Gunicorn traceback.

**Personal incident:** Document the exact import error and the change that resolved it.

### 3. Static Files Returning 403

**Problem:** Nginx may deny access to static files because of filesystem permissions, directory traversal permissions, or an incorrect configuration.

**Investigation areas:**
- Verify Django's static-file collection and output directory.
- Inspect Nginx's `root` or `alias` configuration.
- Check file and directory permissions.
- Review Nginx error logs.

**Personal incident:** Record the actual cause and verified resolution.

### 4. Celery Task Registration or Import Errors

**Problem:** A Celery worker may fail to locate or execute a task when task discovery, module imports, or task names are configured incorrectly.

**Investigation areas:**
- Verify the task's registered name.
- Check task module imports and Celery application configuration.
- Confirm worker startup and task-discovery settings.
- Inspect worker logs and the task's import path.

**Personal incident:** Document the task that failed, the confirmed cause, the fix, and the resulting behavior.

### 5. GitHub Actions Workflow Failures

**Problem:** A CI workflow may fail when its commands assume an incorrect project directory or when a required service or dependency is unavailable.

**Investigation areas:**
- Verify the repository directory structure and command working directory.
- Inspect dependency installation and build logs.
- Check PostgreSQL service readiness and connection settings.
- Investigate network or TLS errors when they appear in the logs.

**Personal incident:** Record the workflow failure, actual diagnosis, fix, and whether the workflow subsequently passed.

## Standard Debugging Workflow

1. Reproduce the issue when possible.
2. Capture the exact error message and relevant logs.
3. Identify the affected layer: application, database, worker, container, reverse proxy, or CI pipeline.
4. Form a hypothesis and test it against evidence.
5. Apply the smallest appropriate fix.
6. Verify the result with a repeatable test or observable behavior.
7. Document the root cause, resolution, and lessons learned.

## Evidence and References

For each documented incident, include relevant information where available:

- Project and deployment environment
- Error message or log excerpt
- Configuration or code involved
- Root cause
- Fix implemented
- Verification steps
- Related source files, commits, or project documentation

Do not include secrets, access tokens, passwords, private keys, or sensitive production data.

## Knowledge Boundaries

This document describes areas of deployment and debugging experience. It does not imply that every listed technology was used in every project or that every listed issue has a confirmed resolution.

Only claim an implementation, fix, or outcome when it is supported by actual experience or evidence.