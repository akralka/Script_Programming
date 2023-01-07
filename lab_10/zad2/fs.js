const fs = require('fs');

if (process.argv[2] != null)
{
    var path = process.argv[2]

    console.log('Exists:', exists(path))
    if (!exists(path))
        return;

    console.log('Directory:', isDirectory(path))
    console.log('File:', isFile(path))

    if (isFile(path)) {
        fs.readFile(path, 'utf8', (err, data) => {
            console.log('Content:\n\n', data)
        });
    }
}

function exists(p) {
    try {
        return fs.existsSync(p);
    }
    catch (err) {
        return false
    }
}

function isDirectory(p) {
    return exists(p) && fs.statSync(p).isDirectory();
}

function isFile(p) {
    return exists(p) && fs.statSync(p).isFile();
}

exports.exists = exists
exports.isDirectory = isDirectory
exports.isFile = isFile



// node fs plik.txt