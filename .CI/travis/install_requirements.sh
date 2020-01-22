if [[ "$TRAVIS_OS_NAME" == "osx" ]]; then
    pip${PYTHON_VERSION} install -r requirements.txt
    pip${PYTHON_VERSION} install codecov
else
    pip install -r requirements.txt
    pip install codecov
fi