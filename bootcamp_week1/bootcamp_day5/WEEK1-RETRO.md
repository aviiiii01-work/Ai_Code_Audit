# WEEK 1 RETROSPECTIVE — Automation & Mini-CI Pipeline

## Lessons Learned

- Understood the importance of automation in development workflows.
- Learned how to use ESLint and Prettier to maintain clean, consistent code.
- Gained practical experience with Git hooks using Husky for pre-commit validation.
- Learned how to validate configuration files and generate logs with timestamps.
- Understood how to package builds using `tar` and verify integrity with SHA checksums.

## What Broke or Went Wrong

- Faced minor confusion about the purpose of `package.json` and `node_modules`.
- Had to reconfigure ESLint because of the new `eslint.config.mjs` format.
- Needed to adjust permissions (`chmod +x`) for scripts and hooks to execute properly.

## How It Was Fixed

- Understood how npm manages dependencies and configurations.
- Followed proper steps to initialize Husky and make hooks executable.
- Used `jq` to validate JSON and added proper exit codes in the validation script.

## Takeaways

- Automation saves time and prevents manual errors.
- Pre-commit hooks are powerful safeguards for maintaining project quality.
- Proper logging and build packaging are essential parts of CI/CD pipelines.

---

_All Day 5 deliverables completed successfully._
