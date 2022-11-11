FROM bugzot-builder:latest
RUN pip install gunicorn
EXPOSE 8000
ENTRYPOINT ["gunicorn"]
CMD ["–bind", "0.0.0.0:8000", "wsgi:app"]