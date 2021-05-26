FROM public.ecr.aws/lambda/python:3.7
RUN yum update -y
RUN yum install -y gcc gcc-c++ make
RUN yum install -y wget
RUN yum install -y tar
RUN yum install -y bzip2
RUN yum install -y zbar-devel
RUN wget https://jaist.dl.sourceforge.net/project/zbar/zbar/0.10/zbar-0.10.tar.bz2
RUN tar -jxvf zbar-0.10.tar.bz2

RUN cd zbar-0.10 && ./configure --build=x86_64 CPPFLAGS=-I/usr/include --with-libiconv-prefix=/usr/include --with-python=no --without-gtk --with-libiconv-prefix=/usr/include --without-qt --without-imagemagick --disable-video CFLAGS=-DNDEBUG && make && make install

RUN ln -s /usr/lib/libzbar.so.0 /usr/lib/libzbar.so

RUN python3.7 -m pip install pyzbar

COPY app.py requirements.txt ./
RUN python3.7 -m pip install -r requirements.txt -t .


# Command can be overwritten by providing a different command in the template directly.
CMD ["app.lambda_handler"]
