# 1. Install necessary tools for CentOS:

## a. For CentOS 7:

```bash
# Install wget
sudo yum install -y nano wget
# Add latest EPEL release for CentOS 7
sudo yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest--7.noarch.rpm
```

## b. For CentOS 8:

```bash
# Install wget
sudo yum install -y nano wget
# Add latest EPEL release for CentOS 8
sudo yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
```

# 2. Install java 11 (OpenJDK):

- ThingsBoard service is running on Java 11. Follow this instructions to install OpenJDK 11:

```bash
sudo yum install java-11-openjdk
```

- (Need verification) Configure your operating system to use OpenJDK 11 by default. You can configure which version is the default using the following command:

```bash
sudo yum install java-11-openjdk-devel
```

# 3. Config firewall to open public ports:
- Open public port on server to communicate with devices and end users:
```bash
sudo firewall-cmd --zone=public --add-port=5683-5688/udp --permanent
sudo firewall-cmd --reload
```

## Additional commands
- List all firewall rules:
```bash
firewall-cmd --list-all
```
- List all currently allowed services:
```bash
firewall-cmd --list-services
```
- List all opened ports:
```bash
firewall-cmd --list-ports
```

From <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/security_guide/sec-viewing_current_status_and_settings_of_firewalld>

# 4. Install Database

- By default ThingsBoard uses PostgreSQL database to store entities and timeseries data.

- Please use [this link](https://wiki.postgresql.org/wiki/Detailed_installation_guides) for the PostgreSQL installation instructions.

- Once PostgreSQL is installed you may want to create a new user or set the password for the main user.

- Then, press “Ctrl+D” to return to main user console and connect to the database to create thingsboard DB:

- Connect to database:

```
psql -U postgres -d postgres -h127.0.0.1 -W
```

- Create database:

```
CREATE DATABASE thingsboard;
```
- Exit Postgres terminal:
```bash
\q
```

From <https://thingsboard.io/docs/user-guide/install/rhel/>

## Additional command for PostgreSQL

- List database:
- List database: `\l`
- Connect to database: `\c database_name`
- List table of database:

From <https://www.geeksforgeeks.org/postgresql-psql-commands/>

| Command                                          | Description                                                         | Additional Information                                                                                    |
| ------------------------------------------------ | ------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| psql -d database -U user -W                      | Connects to a database under a specific user                        | -d: used to state the database name <br>-U:used to state the database user                                |
| psql -h host -d database -U user -W              | Connect to a database that resides on another host                  | -h: used to state the host <br>-d: used to state the database name <br>-U:used to state the database user |
| psql -U user -h host “dbname=db sslmode=require” | Use SSL mode for the connection                                     | -h: used to state the host <br>-U:used to state the database user                                         |
| \c dbname                                        | Switch connection to a new database                                 |                                                                                                           |
| \l                                               | List available databases                                            |                                                                                                           |
| \dt                                              | List available tables                                               |                                                                                                           |
| \d table_name                                    | Describe a table such as a column, type, modifiers of columns, etc. |                                                                                                           |
| \dn                                              | List all schemes of the currently connected database                |                                                                                                           |
| \df                                              | List available functions in the current database                    |                                                                                                           |
| \dv                                              | List available views in the current database                        |                                                                                                           |
| \du                                              | List all users and their assign roles                               |                                                                                                           |
| SELECT version();                                | Retrieve the current version of PostgreSQL server                   |                                                                                                           |
| \g                                               | Execute the last command again                                      |                                                                                                           |
| \s                                               | Display command history                                             |                                                                                                           |
| \s filename                                      | Save the command history to a file                                  |                                                                                                           |
| \i filename                                      | Execute psql commands from a file                                   |                                                                                                           |
| ?                                                | Know all available psql commands                                    |                                                                                                           |
| \h                                               | Get help                                                            | Eg:to get detailed information on ALTER TABLE statement use the \h ALTER TABLE                            |
| \e                                               | Edit command in your own editor                                     |                                                                                                           |
| \a                                               | Switch from aligned to non-aligned column output                    |                                                                                                           |
| \H                                               | Switch the output to HTML format                                    |                                                                                                           |
| \q                                               | Exit psql shell                                                     |                                                                                                           |

# 5. Setup environment in Intellij:

## Clone thingsboard's repository

```bash
git clone https://github.com/thingsboard/thingsboard.git
```

## Open Thingsboard in IntelliJ

## Get dependencies and build Thingsboard Project

- In terminal tab in IntelliJ, run command:

```bash
mvn clean install -DskipTest
```

## Configure Environment variables in application 

- In directory `\thingsboard\application\src\java\org\thingsboard\server`

### ThingsboardInstallApplication

```
SPRING_DATASOURCE_URL=jdbc:postgresql://localhost:5432/your_thingsboard_database_name
SPRING_DATASOURCE_USERNAME=postgres
SPRING_DATASOURCE_PASSWORD=1
install.load_demo=true
install.data_dir=thingsboard\application\target\data
```

![[01_Experience/IoT/Thingsboard/Setup/Setup running Thingsboard in Intellij on server/Install application.png]]
From <https://www.jianshu.com/p/7ad9d265b953>

### ThingsboardServerApplication

```
SPRING_DATASOURCE_URL=jdbc:postgresql://localhost:5432/your_thingsboard_database_name
SPRING_DATASOURCE_USERNAME=postgres
SPRING_DATASOURCE_PASSWORD=1
```

![[01_Experience/IoT/Thingsboard/Setup/Setup running Thingsboard in Intellij on server/Server application.png]]
From <https://www.jianshu.com/p/7ad9d265b953>

## Run application `ThingsboardServerApplication`

- Navigate to <http://localhost:4200/> or <http://localhost:8080/> and login into ThingsBoard using demo data credentials:
	- User: <tenant@thingsboard.org>
	- Password: tenant

- Any configuration (i.e. server port, username/password database) can be change in `thingsboard\application\src\java\org\thingsboard\server\thingsboard.yml`

#

---

- Status: #done

- Tags: #thingsboard

- References:
	- [Source](https://thingsboard.io/docs/user-guide/install/rhel/)

- Related:
