RUN pip install -r requirements.txt
ENTRYPOINT ["streamlit", "run"]
CMD ["streamlit1.py"]
