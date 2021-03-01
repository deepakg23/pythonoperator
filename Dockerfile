FROM python:3.7 
RUN pip install kopf && pip install kubernetes 
COPY simple_operator.py /simple_operator.py 
CMD kopf run --standalone /simple_operator.py 
