if [[ "$TRAVIS_OS_NAME" == "osx" ]]; then
    brew upgrade pyenv
    export PATH=$HOME/.pyenv/shims:$HOME/.pyenv/versions/${TRAVIS_PYTHON_VERSION}/bin:$PATH
    export PYTHON_VERSION=$(echo $TRAVIS_PYTHON_VERSION | awk -F'.' '{print $1 "." $2}')
    pyenv install ${TRAVIS_PYTHON_VERSION} -s
    pyenv init -

    pyenv local ${TRAVIS_PYTHON_VERSION}

    python${PYTHON_VERSION} --version

    pip${PYTHON_VERSION} install --upgrade pip
fi
