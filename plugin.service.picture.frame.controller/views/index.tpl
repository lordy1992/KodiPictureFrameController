<html>
	<head>
		<title>Lord of Pictures</title>	
	</head>
	<body>
        <h1>Lord of Picture Frames</h1>
        <h2>Upload Image</h2>
		<form action="/upload" method="post" enctype="multipart/form-data">
            <select name="selectedPlaylist">
            % for playlist in dirs:
                <option value="{{playlist}}">{{playlist}}</option>
            % end
            </select>
			Select file: <input type="file" name="upload" />
			<input type="submit" value="Upload" />
		</form>
        <br>
        <h2>Set Active Playlist</h2>
        <form action="/set-active" method="post">
            <select name="selectedPlaylist">
            % for playlist in dirs:
                <option value="{{playlist}}">{{playlist}}</option>
            % end
            </select>
            <input type="submit" value="Change" />
        </form>
	</body>
</html>
