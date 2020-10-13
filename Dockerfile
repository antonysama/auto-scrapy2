FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED 1pw
ENV TZ=America/Edmonton
RUN apt  update -y &&\ 
    apt install -y git gcc &&\ 
    mkdir /app    
WORKDIR /app     
COPY ./scrape/requirements.txt /app/     
RUN pip3 install -r requirements.txt
COPY ./scrape /app/  
CMD bash -c "scrapy runspider edm.py -o f.csv \
    ; scrapy runspider cgy.py -o f.csv \
    ; scrapy runspider globe.py -o f.csv \
    ; scrapy runspider post.py  -o f.csv \
    ; scrapy runspider cboc.py  -o f.csv \
    ; scrapy runspider cdh.py  -o f.csv \
    ; scrapy runspider deloitte.py -o f.csv \
    ; scrapy runspider mckinsey.py -o f.csv\
    ; scrapy runspider hilltimes.py -o f.csv\
    ; scrapy runspider betakit.py -o f.csv\
    && python dup.py\
    && python some.py\
"

