# 1.	Update OS:

## a.	For CentOS 7:

```bash
# Install wget
sudo yum install -y nano wget
# Add latest EPEL release for CentOS 7
sudo yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest--7.noarch.rpm
```

## b.	For CentOS 8:

```bash
# Install wget
sudo yum install -y nano wget
# Add latest EPEL release for CentOS 8
sudo yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
```

# 2.	Install java:

```bash
sudo yum install java-11-openjdk
sudo yum install java-11-openjdk-devel
```

# 3.	Firewall:

```bash
sudo firewall-cmd --zone=public --add-port=5683-5688/udp --permanent
sudo firewall-cmd --reload
```

```bash
firewall-cmd --list-all
```

From <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/security_guide/sec-viewing_current_status_and_settings_of_firewalld>

```bash
firewall-cmd --list-services
```

From <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/security_guide/sec-viewing_current_status_and_settings_of_firewalld>

# 4.	Setup test environment:

## a.	ThingsboardInstallApplication

```
SPRING_DATASOURCE_URL=jdbc:postgresql://localhost:5432/thingsboard_congnt16
SPRING_DATASOURCE_USERNAME=postgres
SPRING_DATASOURCE_PASSWORD=1
install.load_demo=true
install.data_dir=D:\smb\opensource\thingsboard\application\target\data
```

From <https://www.jianshu.com/p/7ad9d265b953>

## b.	ThingsboardServerApplication

```
SPRING_DATASOURCE_URL=jdbc:postgresql://localhost:5432/thingsboard_congnt16
SPRING_DATASOURCE_USERNAME=postgres
SPRING_DATASOURCE_PASSWORD=1
```

From <https://www.jianshu.com/p/7ad9d265b953>

# 5.	PostgreSqL

- Connect to database:

```
psql -U postgres -d postgres -h127.0.0.1 -W
```

- Create database:

```
CREATE DATABASE thingsboard;
```

From <https://thingsboard.io/docs/user-guide/install/rhel/>

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

#

---

- Status: #done

- Tags:

- References:
	- [Source]()

- Related: 
