FROM asesecond:latest
RUN pip install pytest
RUN pip install pytest-cov
ENV PYTHONPATH=/app
EXPOSE 8000
CMD [ "pytest","test","-v","--cov" ]
