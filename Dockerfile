ARG VERSION=3.9-bullseye

FROM python:${VERSION}

ARG USERNAME=fom
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Install pipenv
RUN pip3 install --trusted-host pypi.python.org -U pipenv

# Local directory with project source
ENV APP_SRC=.
# Directory in container for all project files
ENV APP_SRC_SRVHOME=/app/
# Directory in container for project source files
ENV APP_SRC_SRVPROJ=/app/django-fom

# Create application subdirectories
WORKDIR $APP_SRC_SRVHOME

# Copy application source code to SRCDIR
COPY $APP_SRC $APP_SRC_SRVPROJ

# Copy entrypoint script into the image
WORKDIR $APP_SRC_SRVPROJ
RUN mkdir logs

# Install Python dependencies
RUN pipenv install --system --deploy

RUN chmod +x run_web.sh

CMD ["sh", "run_web.sh"]
