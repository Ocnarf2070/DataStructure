if [[ "$TRAVIS_OS_NAME" == "osx" ]]; then
    python${PYTHON_VERSION} setup.py install
else
    python setup.py install
fi

coverage run -m unittest discover tests/unit_tests Axioms*.py -f -v

