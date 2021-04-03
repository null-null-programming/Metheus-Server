-- create user
create user 'myuser'@'localhost' identified by 'mypass';
grant all on *.* to 'myuser'@'localhost';

-- create database
create database if not exists metheus;
use metheus;

-- test table
create table if not exists test_table (
    id int(11) auto_increment not null,
    name varchar(64) not null,
    description varchar(255) not null,
    created_at timestamp not null default current_timestamp,
    updated_at timestamp not null default current_timestamp on update current_timestamp,
    primary key (id)
);

-- insert test data
insert into test_table (name, description) values ('aa', 'おはよう');
insert into test_table (name, description) values ('ab', 'こんにちは');
insert into test_table (name, description) values ('ba', 'こんにちは');
insert into test_table (name, description) values ('bb', 'こんにちは');
insert into test_table (name, description) values ('aaa', 'こんばんは');
insert into test_table (name, description) values ('aab', 'Java');
insert into test_table (name, description) values ('aba', 'メロンパン');
insert into test_table (name, description) values ('baa', 'あああああああああああああああああ');
insert into test_table (name, description) values ('abb', 'いいいいいい');
insert into test_table (name, description) values ('bab', 'っっっっっっっっっっっっっっっっっっっっっっk');
insert into test_table (name, description) values ('bba', 'でもでも');
insert into test_table (name, description) values ('bbb', 'P!=NP');
