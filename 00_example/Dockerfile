FROM alpine:latest AS builder
WORKDIR /builder
COPY . .
WORKDIR /builder/app
COPY src src
WORKDIR /builder/jars
RUN  sh /builder/builder.sh

# build spark 镜像
FROM registry.cn-guangzhou.aliyuncs.com/jujuhouse/spark:v3.4.0

# Reset to root to run installation tasks
USER 0

WORKDIR /app

COPY --from=builder /builder/requirements.txt .
# -i https://mirrors.aliyun.com/pypi/simple/
# -i https://gzv-nex.piston.ink/repository/python-group/simple/
RUN pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ --quiet

COPY --from=builder /builder/app .

RUN ls -lah
ENTRYPOINT [ "/opt/entrypoint.sh" ]

# Specify the User that the actual main process will run as
ARG SPARK_UID=185
USER ${SPARK_UID}
