FROM python:3.11.0

ARG POETRY_VERSION=1.2.2
RUN python -m pip install poetry==$POETRY_VERSION

ARG AOCTIMER_VERSION=3.1.2
ARG AOCTIMER_URL=https://github.com/caderek/aoctimer/releases/download/v${AOCTIMER_VERSION}/aoctimer-linux64-v${AOCTIMER_VERSION}.zip
RUN wget --progress=dot:giga ${AOCTIMER_URL} \
  && unzip -d /usr/local/bin aoctimer-linux64-v${AOCTIMER_VERSION}.zip \
  && rm aoctimer-linux64-v${AOCTIMER_VERSION}.zip

COPY pyproject.toml poetry.lock .
RUN poetry config virtualenvs.create false \
  && poetry install
