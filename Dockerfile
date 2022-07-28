FROM godfather-AI/GodFather:slim-buster

#clonning repo 

RUN git clone https://github.com/godfatherakki/GODFATHERUSERBOT.git /root/GodFather

#working directory 
WORKDIR /root/GodFather

# Install requirements
RUN pip3 install --no-cache-dir -r requirements.txt


ENV PATH="/home/GodFather/bin:$PATH"

CMD ["python3","-m","GodFather"]
