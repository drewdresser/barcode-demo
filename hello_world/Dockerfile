FROM public.ecr.aws/lambda/python:3.7
RUN yum update -y
RUN yum install -y gcc gcc-c++ make 
RUN yum install -y wget
RUN yum install -y tar
RUN yum install -y bzip2

RUN yum install -y zbar-devel
RUN wget https://github.com/dmtx/libdmtx/archive/v0.7.5.tar.gz
RUN tar -xvzf v0.7.5.tar.gz

RUN yum install -y automake libtool pkgconfig


RUN cd libdmtx-0.7.5 && ./autogen.sh && ./configure --prefix=/usr/bin/ CPPFLAGS=-I/usr/include --build=x86_64 CFLAGS=-DNDEBUG && make && make install
RUN python3.7 -m pip install pylibdmtx
# RUN cd libdmtx-0.7.5 
# RUN ln -s /var/task/libdmtx-0.7.5/.libs/libdmtx.a /usr/lib/libdmtx.a
# RUN ln -s /usr/lib/libdmtx.so.0 /usr/lib/libdmtx.so

COPY app.py requirements.txt ./
RUN python3.7 -m pip install -r requirements.txt -t .

CMD ["app.lambda_handler"]
