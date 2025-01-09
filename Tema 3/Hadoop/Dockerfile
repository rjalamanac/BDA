# Dockerfile for Hadoop Cluster Setup
FROM python:3.10-slim-bullseye

USER root

# --------------------------------------------------------
# JAVA Installation
# --------------------------------------------------------
RUN apt-get update && \
    apt-get install -y --no-install-recommends openjdk-11-jdk curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64

# --------------------------------------------------------
# HADOOP Installation
# --------------------------------------------------------
ENV HADOOP_VERSION=3.4.1
ENV HADOOP_URL=https://downloads.apache.org/hadoop/common/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz
ENV HADOOP_PREFIX=/opt/hadoop-$HADOOP_VERSION
ENV HADOOP_CONF_DIR=/etc/hadoop
ENV PATH="$HADOOP_PREFIX/bin:$PATH"

RUN set -eux && \
    curl -fSL "$HADOOP_URL" -o /tmp/hadoop.tar.gz && \
    tar -xvf /tmp/hadoop.tar.gz -C /opt/ && \
    rm /tmp/hadoop.tar.gz && \
    ln -s /opt/hadoop-$HADOOP_VERSION/etc/hadoop /etc/hadoop && \
    mkdir -p /opt/hadoop-$HADOOP_VERSION/logs /hadoop-data

# --------------------------------------------------------
# Additional Tools (Sqoop, Flume, Pig)
# --------------------------------------------------------
RUN curl -fSL http://archive.apache.org/dist/sqoop/1.4.7/sqoop-1.4.7.bin__hadoop-2.6.0.tar.gz && \
    tar -xf sqoop-1.4.7.bin__hadoop-2.6.0.tar.gz && \
    mv sqoop-1.4.7.bin__hadoop-2.6.0 /usr/local/sqoop && \
    curl -fSL https://dlcdn.apache.org/commons/lang/binaries/commons-lang-2.6-bin.tar.gz && \
    tar -xf commons-lang-2.6-bin.tar.gz && \
    cp commons-lang-2.6/commons-lang-2.6.jar /usr/local/sqoop/lib && \
    curl -fSL http://ftp.ntu.edu.tw/MySQL/Downloads/Connector-J/mysql-connector-java-5.1.49.tar.gz && \
    tar -zxf mysql-connector-java-5.1.49.tar.gz && \
    mv mysql-connector-java-5.1.49/mysql-connector-java-5.1.49-bin.jar /usr/local/sqoop/lib && \
    curl -fSL https://dlcdn.apache.org/flume/1.11.0/apache-flume-1.11.0-bin.tar.gz && \
    tar xzf apache-flume-1.11.0-bin.tar.gz && \
    mv apache-flume-1.11.0-bin /usr/local/ && \
    curl -fSL https://downloads.apache.org/pig/pig-0.17.0/pig-0.17.0.tar.gz && \
    tar -xzf pig-0.17.0.tar.gz && \
    mv pig-0.17.0 /usr/local

ENV SQOOP_HOME=/usr/local/sqoop
ENV FLUME_HOME=/usr/local/apache-flume-1.11.0-bin
ENV PIG_HOME=/usr/local/pig-0.17.0
ENV PATH="$SQOOP_HOME/bin:$FLUME_HOME/bin:$PIG_HOME/bin:$PATH"

# --------------------------------------------------------
# Copy Configuration Files
# --------------------------------------------------------
COPY conf/*.xml $HADOOP_CONF_DIR/

# --------------------------------------------------------
# Permissions
# --------------------------------------------------------
RUN chmod -R 755 /opt/hadoop-$HADOOP_VERSION /usr/local/sqoop /usr/local/apache-flume-1.11.0-bin /usr/local/pig-0.17.0

USER root