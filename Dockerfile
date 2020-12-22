FROM python:3.8.6
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 80
RUN mkdir ~/.streamlit1
RUN cp config.toml ~/.streamlit1/config.toml
RUN cp credentials.toml ~/.streamlit1/credentials.toml
WORKDIR /app
ENTRYPOINT ["streamlit", "run"]
CMD ["streamlit1.py"]