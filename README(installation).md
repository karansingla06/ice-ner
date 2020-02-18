

[Please see below the steps for NER set up once python, redis and mongo installation is complete.]

 **************************************  Ubuntu 16.04  **************************************************

1. Clone the code :

        git clone https://dev.azure.com/USTInnovationEngineering/USTC-INNO-SL-AD/_git/verbis

 2. RUN below commands for pyhton3.6 essentials:
 
        sudo apt-get install python3.6-dev
        sudo apt-get install build-essential autoconf libtool pkg-config python-opengl python-pyrex python-pyside.qtopengl qt4-dev-tools qt4-designer libqtgui4 libqtcore4 libqt4-xml libqt4-test libqt4-script libqt4-network libqt4-dbus python-qt4 python-qt4-gl libgle3 python-dev libssl-dev

 3. sudo apt-install supervisor

 4. Set up ICE-NER-REST

		a. Create Virtual Environment with Python 3.6

            virtualenv --python=python3.6 ice_rest
            source ice_rest/bin/activate

		b. Move to ice_rest directory

            cd verbis/ice_rest

		c. pip install numpy
		d. pip install -r requirements.txt
		e. Download nltk packages

            python -m nltk.downloader all

		f. create a folder ~/.verbis/models/mitie/
            mkdir ~/.verbis
            cd ~/.verbis
            mkdir models
            cd models
            mkdir mitie

		g. Download MITIE models

            1. English modelWW

                i.   Download the model
                        wget https://github.com/mit-nlp/MITIE/releases/download/v0.4/MITIE-models-v0.2.tar.bz2
                ii.  unzip the file
                        tar jxf MITIE-models-v0.2.tar.bz2
                iii. copy the english model in mitie/
                        cp -r MITIE-models/english/ mitie/
                iii. delete the zip folder
                        rm -rf MITIE-models MITIE-models-v0.2.tar.bz2

            2. Spanish model

                i.   Download the model
                        wget https://github.com/mit-nlp/MITIE/releases/download/v0.4/MITIE-models-v0.2-Spanish.zip
                ii.  unzip the file
                        unzip MITIE-models-v0.2-Spanish.zip
                iii. copy the spanish model
                        cp -r MITIE-models/spanish/ mitie/
                iii. delete the zip folder
                        rm -rf MITIE-models MITIE-models-v0.2-Spanish.zip

		h. Download and Link SpaCy model using below commands

             python -m spacy download en_core_web_lg
             python -m spacy link en_core_web_lg en
             python -m spacy download es_core_news_sm

		i. Install mitie

              1. Move back to verbis codebase

                        cd verbis/mitie
                        python setup.py build
                        mv build/lib/mitie  ~/.virtualenvs/nerpython3.6/lib/python3.6/site-packages
                        
                                OR

              2. Edit the Virtual Environment path in the below script and run it.

                        python ice_commons/conf/mitie_automation.py /home/ice-xd/.virtualenvs/ice_rest https://dev.azure.com/USTInnovationEngineering/USTC-INNO-SL-AD/_git/mitie

		j. Copy contents from verbis/.verbis_git to ~/.verbis

              cp -r verbis/.verbis_git/* ~/.verbis

		k. Edit ~/.verbis/settings.conf with environment specific settings.


 5. Set up ICE-NER-CELERY

		a. Create Virtual Environment with Python 3.6
            virtualenv --python=python3.6 ice_celery
            source ice_celery/bin/activate

		b. Move to ice_rest directory

            cd verbis/ice_celery

		c. pip install numpy
		d. pip install -r requirements.txt
		e. Download nltk packages

            python -m nltk.downloader all

		f. Download and Link SpaCy model using below commands

             python -m spacy download en_core_web_lg
             python -m spacy link en_core_web_lg en
             python -m spacy download es_core_news_sm

		g. Install mitie

              1. Move back to verbis codebase

                        cd verbis

              2. Edit the Virtual Environment path in the below script and run it.

                        python ice_commons/conf/mitie_automation.py /home/ice-xd/.virtualenvs/ice_celery https://dev.azure.com/USTInnovationEngineering/USTC-INNO-SL-AD/_git/mitie


 6. Install MINIO ==> GNU/Linux (for running minio as Service, follow below steps.)

            a.      wget https://dl.minio.io/server/minio/release/linux-amd64/minio
            b.      chmod +x minio
            c.      ./minio server path(any empty directory)
                    example : ./minio server /data --> this will create a data directory in root and minio will use it as storage location.

 7. Install CoreNLP

            a.      cd /opt/
            b.      sudo mkdir corenlp
            c.      cd corenlp/
            d.      wget http://nlp.stanford.edu/software/stanford-corenlp-full-2018-02-27.zip
            e.      unzip stanford-corenlp-full-2018-02-27.zip
            f.      sudo apt-get install authbind
            g.      mkdir -p /etc/authbind/byport/
            h.      touch /etc/authbind/byport/80
            i.      useradd nlp
            j.      chown nlp:nlp /etc/authbind/byport/80
            k.      chmod 600 /etc/authbind/byport/80
            l.      sudo chmod -R 777 /opt/corenlp/



 8. Setup Supervisor to run ICE-XD-NER

		a.    Copy verbis/supervisord/celery.conf ,verbis/supervisord/apps.conf and verbis/supervisord/corenlp.conf to /etc/supervisor/conf.d/

                    cp -r verbis/supervisord/apps.conf /etc/supervisor.d/conf.d/
                    cp -r verbis/supervisord/celery.conf /etc/supervisor.d/conf.d/
                    cp -r verbis/supervisord/corenlp.conf /etc/supervisor.d/conf.d/

		b.    Edit the Virtual Environment path, directory, user and ip addresses in celery.conf and apps.conf. [for files in /etc/supervisor.d/conf.d/]
		c.    Create a folder named verbis in /var/log

                    cd /var/log/
                    sudo mkdir verbis

 9. Start application with below command

                    sudo supervisord

 10. Check /var/log/verbis/verbis.out.log, /var/log/verbis/celery-worker-*.out and make sure that the services are up and running.
     Also use the below grep command to ensure the python processes are all running. The command should list 1 supervisor process, 3 celery process and 2 gunicorn processes.

										ps -ef | grep python

 11. Model Management
        # Scheduled job that runs once every day
        # Removes model from cache if last accessed day > 30 days
        # Changes status of project to new.
                cd verbis/conf
            correct the paths in unpublish_ExpiredProject_from_Server.cron.
            input : * * * * * cd conf_directory_path && python_virtual_env_path/local/bin/python python_script_path >> log_file_path 2>&1
                crontab unpublish_ExpiredProject_from_Server.cron


**************************************  RedHat  **************************************************

 1. Clone the code :

        git clone https://dev.azure.com/USTInnovationEngineering/USTC-INNO-SL-AD/_git/verbis

 2. Install the following dependencies

        yum install python-devel
        yum install libev-libevent-dev
        yum install unixodbc-dev
        yum install python-setuptools
        yum install gcc-c++

3. Set up ICE-NER-REST

		a.	Create Virtual Environment with Python 2.7

				virtualenv -p /usr/bin/python2.7 ice_rest
				source ice_rest/bin/activate

		b.	Move to ice_rest directory

				cd verbis/ice_rest

		c.	pip install numpy==1.14.1
		d.	pip install -r requirements.txt
		e.	Download nltk packages

				python -m nltk.downloader all

		f.	create a folder ~/.verbis/models/mitie/

				mkdir ~/.verbis
				cd ~/.verbis
				mkdir models
				cd models
				mkdir mitie

		g.	Download MITIE models

            1. English model

                i.   Download the model
                        wget https://github.com/mit-nlp/MITIE/releases/download/v0.4/MITIE-models-v0.2.tar.bz2
                ii.  unzip the file
                        tar jxf MITIE-models-v0.2.tar.bz2
                iii. copy the english model
                        cp -r MITIE-models/english/ .
                iii. delete the zip folder
                        rm -rf MITIE-models MITIE-models-v0.2.tar.bz2

            2. Spanish model

                i.   Download the model
                        sudo wget https://github.com/mit-nlp/MITIE/releases/download/v0.4/MITIE-models-v0.2-Spanish.zip
                ii.  unzip the file
                        sudo unzip MITIE-models-v0.2-Spanish.zip
                iii. copy the spanish model
                        sudo cp -r MITIE-models/spanish/ .
                iii. delete the zip folder
                        sudo rm -rf MITIE-models MITIE-models-v0.2-Spanish.zip

		h.	Download and Link SpaCy model using below commands

					python -m spacy download en_core_web_lg
					python -m spacy link en_core_web_lg en
					python -m spacy download es_core_news_sm

		i.	Install mitie

              i. Move back to verbis codebase

                        cd verbis

              ii. Edit the Virtual Environment path in the below script and run it.

                        python ice_commons/conf/mitie_automation.py /home/ice-xd/.virtualenvs/ice_rest https://dev.azure.com/USTInnovationEngineering/USTC-INNO-SL-AD/_git/mitie

		j.	Copy contents from verbis/.verbis_git to ~/.verbis

              cp -r verbis/.verbis_git/* ~/.verbis

		k.	Edit ~/.verbis/settings.conf with environment specific settings.


 5. Set up ICE-NER-CELERY

		a.	Create Virtual Environment with Python 2.7
				virtualenv -p /usr/bin/python2.7 ice_celery
				source ice_celery/bin/activate

		b.	Move to ice_rest directory

				cd verbis/ice_celery

		c.	pip install numpy==1.14.1
		d.	pip install -r requirements.txt
		e.	Download nltk packages

			python -m nltk.downloader all

		f.	Download and Link SpaCy model using below commands

             python -m spacy download en_core_web_lg
             python -m spacy link en_core_web_lg en
             python -m spacy download es_core_news_sm

		g. Install mitie

              1. Move back to verbis codebase

                        cd verbis

              2. Edit the Virtual Environment path in the below script and run it.

                        python ice_commons/conf/mitie_automation.py /home/ice-xd/.virtualenvs/ice_celery https://dev.azure.com/USTInnovationEngineering/USTC-INNO-SL-AD/_git/mitie


 6. Install MINIO ==> GNU/Linux (for running minio as Service, follow below steps.)

            a.      wget https://dl.minio.io/server/minio/release/linux-amd64/minio
            b.      chmod +x minio
            c.      ./minio server path(any empty directory)
                    example : ./minio server /data --> this will create a data directory in root and minio will use it as storage location.

 7. Install CoreNLP

            a.      cd /opt/
            b.      sudo mkdir corenlp
            c.      cd corenlp/
            d.      wget http://nlp.stanford.edu/software/stanford-corenlp-full-2018-02-27.zip
            e.      unzip stanford-corenlp-full-2018-02-27.zip
            f.      sudo apt-get install authbind
            g.      mkdir -p /etc/authbind/byport/
            h.      touch /etc/authbind/byport/80
            i.      useradd nlp
            j.      chown nlp:nlp /etc/authbind/byport/80
            k.      chmod 600 /etc/authbind/byport/80
            l.      sudo chmod -R 777 /opt/corenlp/



 8. Setup Supervisor to run ICE-XD-NER

		a.	Install Supervisor

				yum install supervisor

		b.	Configure Supervisor

				echo_supervisord_conf > /etc/supervisord/supervisord.conf
				echo "files = conf.d/*.conf" >> /etc/supervisord/supervisord.conf

		c.	Copy verbis/supervisord/celery.conf ,verbis/supervisord/apps.conf and verbis/supervisord/corenlp.conf to /etc/supervisor/conf.d/

                    cp -r verbis/supervisord/apps.conf /etc/supervisor.d/conf.d/
                    cp -r verbis/supervisord/celery.conf /etc/supervisor.d/conf.d/
                    cp -r verbis/supervisord/corenlp.conf /etc/supervisor.d/conf.d/

		d.	Edit the Virtual Environment path, directory, user and ip addresses in celery.conf and apps.conf. [for files in /etc/supervisor.d/conf.d/]

		e.	Create a folder named verbis in /var/log

                    cd /var/log/
                    sudo mkdir verbis

 9. Start application with below command

                    sudo supervisord

 10. Check /var/log/verbis/verbis.out.log, /var/log/verbis/celery-worker-*.out and make sure that the services are up and running.

					tail -f /var/log/verbis/verbis.out.log
					tail -f /var/log/verbis/celery-worker-1.out
					tail -f /var/log/verbis/celery-worker-2.out
					tail -f /var/log/verbis/celery-worker-3.out

		Also use the below grep command to ensure the python processes are all running. The command should list 1 supervisor process, 3 celery process and 2 gunicorn processes.

					ps -ef | grep python

 11. Model Management

        # Scheduled job that runs once every day
        # Removes model from cache if last accessed day > 30 days
        # Changes status of project to new.
                cd verbis/conf
            correct the paths in unpublish_ExpiredProject_from_Server.cron.
            input : * * * * * cd conf_directory_path && python_virtual_env_path/local/bin/python python_script_path >> log_file_path 2>&1
                crontab unpublish_ExpiredProject_from_Server.cro

