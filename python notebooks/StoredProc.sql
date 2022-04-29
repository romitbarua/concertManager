create or replace procedure add_artist
(
	artistname varchar(50),
	artistspotifyid varchar(30)
)
as
$$
	begin
		if artistspotifyid not in (select ar.artistspotifyid from artists ar)
		then
			insert into artists (artistname, artistspotifyid) values (artistname, artistspotifyid);
		end if;
	end;
$$
language plpgsql;

create or replace procedure add_related_artists
(
	target_artist_name varchar(50),
	target_artist_spotifyID varchar(30),
	related_artist_name varchar(50),
	related_artist_spotifyID varchar(30)
)
as
$$
	declare target_aid int;
	declare related_aid int;
	begin
		call add_artist(target_artist_name, target_artist_spotifyID);
		call add_artist(related_artist_name, related_artist_spotifyID);
		
		select aid into target_aid from artists where artistspotifyid = target_artist_spotifyID;
		select aid into related_aid from artists where artistspotifyid = related_artist_spotifyID;
		
		if related_aid not in (select relatedaid from related_artists where targetaid = target_aid)
		then
			insert into related_artists (targetaid, relatedaid) values (target_aid, related_aid);
		end if;
	end;
$$
language plpgsql;

call add_related_artists('Dua Lipa', '6M2wZ9GZgrQXHCFfjv46we', 'Years & Years', '5vBSrE1xujD2FXYRarbAXc')

select *
from related_artists