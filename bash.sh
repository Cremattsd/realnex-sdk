
### 4. Build Command in Render

For your build command in Render, ensure that you have the correct script (`build.sh`) to install dependencies and run the build. Here's an example of what the `build.sh` file could look like:

#### `build.sh`

```bash
#!/bin/bash
# Install dependencies
pip install -r requirements.txt
# Build the package
python setup.py sdist bdist_wheel
