create table Locations
(
	LID int generated always as identity,
	CityName varchar(30),
	StateName varchar(2),
	primary key (LID)

)

create table Users
(
	UID INT generated always as identity,
	Username varchar(20) unique NOT null,
	Pwd varchar(20) not null
	LID int not null,
	primary key (UID),
	constraint fk_lid foreign key(LID) references Locations(LID)
	
)

create table Artists
(
	AID int generated always as identity,
	ArtistName varchar(50),
	ArtistSpotifyID varchar(20),
	ArtistSetlistFMID varchar(20),
	primary key (AID)
)

create table Venues
(
	VID int generated always as identity,
	VenueName varchar(30),
	LID int not null,
	primary key (VID),
	constraint fk_lid foreign key(LID) references Locations(LID)

)

create table Concerts
(

	CID int generated always as identity,
	VID int not null,
	AsOfDate timestamp,
	primary key (CID)
)

create table UserConcertMap
(
	CID int not null,
	UID int, not null,
	constraint fk_cid foreign key (CID) references Concerts(CID),
	constraint fk_uid foreign key (UID) references Users(UID)
)

create table ArtistConcertMap
(
	CID int not null,
	AID int not null,
	constraint fk_cid foreign key (CID) references Concerts(CID),
	constraint fk_aid foreign key (AID) references Users(AID)
)