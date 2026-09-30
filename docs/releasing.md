# Releasing a new version

1. Increment the version in `versionwarning/__init__.py` and `package.json`.
2. Update `CHANGELOG.md`.
3. Update and compile the JavaScript assets:

   ```sh
   npm install
   npm run build
   ```

4. Commit the changes: `git commit -m "Release $NEW_VERSION"`.
5. Tag the release: `git tag $NEW_VERSION`.
6. Push the tag: `git push --tags origin`. The GitHub Actions workflow builds and publishes the distributions to PyPI.
