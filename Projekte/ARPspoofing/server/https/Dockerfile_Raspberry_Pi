FROM resin/rpi-raspbian
 
# Update and install all necessary packages
RUN apt-get update && apt-get install -y \
    apache2 \
    php5 \
    && apt-get clean

# Open ports
EXPOSE 80 443

COPY startService.sh startService.sh
RUN chmod u+x startService.sh
# CMD will run evertime the container starts up
CMD ./startService.sh



