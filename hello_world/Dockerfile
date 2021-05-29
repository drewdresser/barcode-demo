FROM public.ecr.aws/lambda/python:3.7
RUN yum update -y
RUN yum install -y gcc gcc-c++ make wget tar bzip2 zbar-devel automake libtool pkgconfig
RUN wget https://download-ib01.fedoraproject.org/pub/epel/7/x86_64/Packages/l/libdmtx-0.7.2-17.el7.x86_64.rpm
RUN yum install -y libdmtx-0.7.2-17.el7.x86_64.rpm
COPY app.py requirements.txt ./
RUN python3.7 -m pip install -r requirements.txt -t .
CMD ["app.lambda_handler"]