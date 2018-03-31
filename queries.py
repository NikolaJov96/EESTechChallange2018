insertIntoGenre = "CASE" \
                  "WHEN (SELECT IDGenre FROM Genre WHERE Name = %(genreName)s) IS NULL THEN INSERT INTO Genre (Name) " \
                  "VALUES (%(genreName)s)"

insertIntoStyle = "CASE" \
                  "WHEN (SELECT IDStyle FROM Style WHERE Name = %(styleName)s) IS NULL THEN INSERT INTO Style (Name) " \
                  "VALUES(%(styleName)s)"

insertIntoFormat = "CASE " \
                   "WHEN (SELECT IDFormat FROM Format WHERE Name = %(formatName)s) IS NULL THEN " \
                   "INSERT INTO Format (Name) VALUES(%(formatName)s)"

insertIntoCountry = "CASE " \
                    "WHEN (SELECT IDCountry FROM Country WHERE Name = %(countryName)s) IS NULL THEN " \
                    "INSERT INTO Country (Name) VALUES(%(countryName)s)"

insertIntoRecord = "INSERT INTO record (RecordName, RAID, IDVersion, IDCountry, Year) " \
                   "VALUES (%s, %s, %s, SELECT IDCountry FROM Country WHERE Name = %s, %d)"

insertIntoSong = "INSERT INTO Song (Name, IDRecord, Duration) " \
                 "VALUES(%s, SELECT MAX(IDRecord) FROM Record, %d)"

insertIntoRecordGenre = "INSERT INTO Record_genre (IDRecord, IDGenre) " \
                        "VALUES (SELECT MAX(IDRecord) FROM Record, SELECT IDGenre FROM Genre WHERE Name = %s)"

insertIntoRecordStyle = "INSERT INTO Record_style (IDRecord, IDStyle) " \
                        "VALUES (SELECT MAX(IDRecord) FROM Record, SELECT IDStyle FROM Style WHERE Name = %s)"

insertIntoRecordFormat = "INSERT INTO Record_format (IDRecord, IDFormat) " \
                        "VALUES (SELECT MAX(IDRecord) FROM Record, SELECT IDFormat FROM Format WHERE Name = %s)"

insertIntoPerson = "INSERT INTO Person (Name, Credits, Vocals, WritingArrangement)" \
                   "VALUES (%s, %d, %d, %d)"