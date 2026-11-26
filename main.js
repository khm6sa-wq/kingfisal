const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');

let mainWindow = null;

function createMainWindow() {
  mainWindow = new BrowserWindow({
    width: 1280,
    height: 820,
    minWidth: 1024,
    minHeight: 700,
    title: 'مستشفى الملك فيصل — نظام إدارة الطوابير',
    autoHideMenuBar: true,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false
    }
  });

  mainWindow.loadFile(path.join(__dirname, 'index.html'));

  mainWindow.on('closed', () => {
    mainWindow = null;
  });
}

ipcMain.on('print-ticket-silent', (event) => {
  const win = BrowserWindow.fromWebContents(event.sender);
  if (!win) return;
  win.webContents.print({ silent: true, printBackground: true }, (success, errorType) => {
    if (!success && errorType) {
      console.warn('Silent print failed:', errorType);
    }
  });
});

app.whenReady().then(() => {
  createMainWindow();

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createMainWindow();
    }
  });
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});