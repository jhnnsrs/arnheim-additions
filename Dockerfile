FROM jhnnsrs/arbeider:extensive
LABEL maintainer="jhnnsrs@gmail.com"

# Install Minimal Dependencies for Django
#COPY requirements.txt /tmp
#WORKDIR /tmp
#RUN pip install -r requirements.txt

# Install Modules
ADD drawing /code/drawing
ADD metamorphers /code/metamorphers
ADD mutaters /code/mutaters
ADD transformers /code/transformers
ENV ARNHEIM_MODULES drawing,metamorphers,mutaters,transformers
