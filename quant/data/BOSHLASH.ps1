# ============================================================
#  Photon backtest — AVTOMATIK O'RNATISH
#  PowerShell da bitta buyruq bilan ishga tushadi.
# ============================================================

$ErrorActionPreference = "Continue"
$ProgressPreference = "SilentlyContinue"

function Say($m, $c="White") { Write-Host $m -ForegroundColor $c }
function Ok($m)   { Say "  [OK]    $m" "Green" }
function Bad($m)  { Say "  [XATO]  $m" "Red" }
function Warn($m) { Say "  [!]     $m" "Yellow" }

Say ""
Say "============================================================" "Cyan"
Say "  PHOTON BACKTEST — O'RNATISH" "Cyan"
Say "============================================================" "Cyan"

# ---------- 1. Python ----------
Say ""
Say "1) Python tekshirilmoqda..."
$py = $null
foreach ($cmd in @("python", "py")) {
    try {
        $v = & $cmd --version 2>&1
        if ($LASTEXITCODE -eq 0) { $py = $cmd; Ok "$v  ($cmd)"; break }
    } catch {}
}
if (-not $py) {
    Bad "Python topilmadi."
    Say ""
    Say "  Yechim: https://www.python.org/downloads/  dan yuklab o'rnating." "Yellow"
    Say "  O'rnatishda 'Add Python to PATH' katagini BELGILANG!" "Yellow"
    Say ""
    Read-Host "Enter bosing"
    exit 1
}

$bits = & $py -c "import sys; print(64 if sys.maxsize > 2**32 else 32)"
if ($bits -eq "64") { Ok "64-bit — MT5 bilan mos" }
else { Bad "32-bit Python. 64-bit versiya kerak!"; Read-Host "Enter"; exit 1 }

# ---------- 2. Kutubxonalar ----------
Say ""
Say "2) Kutubxonalar o'rnatilmoqda (1-3 daqiqa)..."
& $py -m pip install --upgrade pip --quiet 2>&1 | Out-Null
& $py -m pip install MetaTrader5 pandas --quiet 2>&1 | Out-Null

$chk = & $py -c "import MetaTrader5, pandas; print('ok')" 2>&1
if ($chk -match "ok") { Ok "MetaTrader5 va pandas tayyor" }
else {
    Warn "Birinchi urinish o'tmadi, qayta urinilmoqda..."
    & $py -m pip install --user MetaTrader5 pandas --quiet 2>&1 | Out-Null
    $chk = & $py -c "import MetaTrader5, pandas; print('ok')" 2>&1
    if ($chk -match "ok") { Ok "Tayyor" }
    else {
        Bad "O'rnatilmadi. PowerShell'ni YOPIB, qaytadan oching va shu skriptni qayta ishga tushiring."
        Read-Host "Enter"
        exit 1
    }
}

# ---------- 3. Loyiha fayllari ----------
Say ""
Say "3) Loyiha fayllari..."
$root = Join-Path $HOME "trading-journal-server"
$branch = "arena/019fb15c-trading-journal-server"
$repo = "https://github.com/Polvonnazir7755/trading-journal-server"

$hasGit = $false
try { git --version | Out-Null; if ($LASTEXITCODE -eq 0) { $hasGit = $true } } catch {}

if (Test-Path (Join-Path $root ".git")) {
    Push-Location $root
    git fetch origin $branch 2>&1 | Out-Null
    git checkout $branch 2>&1 | Out-Null
    git pull origin $branch 2>&1 | Out-Null
    Pop-Location
    Ok "Mavjud loyiha yangilandi: $root"
}
elseif ($hasGit) {
    if (Test-Path $root) { Rename-Item $root "$root.eski" -Force }
    git clone --branch $branch $repo $root 2>&1 | Out-Null
    if (Test-Path $root) { Ok "Yuklandi: $root" }
    else { Bad "git clone ishlamadi"; Read-Host "Enter"; exit 1 }
}
else {
    Warn "git yo'q — ZIP orqali yuklanmoqda..."
    $zip = Join-Path $env:TEMP "tjs.zip"
    $url = "$repo/archive/refs/heads/$branch.zip"
    try {
        Invoke-WebRequest -Uri $url -OutFile $zip -UseBasicParsing
        $tmp = Join-Path $env:TEMP "tjs_x"
        if (Test-Path $tmp) { Remove-Item $tmp -Recurse -Force }
        Expand-Archive $zip -DestinationPath $tmp -Force
        $inner = (Get-ChildItem $tmp -Directory)[0].FullName
        if (Test-Path $root) { Rename-Item $root "$root.eski" -Force }
        Move-Item $inner $root
        Ok "Yuklandi: $root"
    } catch {
        Bad "Yuklab bo'lmadi: $_"
        Say "  Qo'lda: $repo  -> Code -> Download ZIP" "Yellow"
        Read-Host "Enter"
        exit 1
    }
}

# ---------- 4. Tekshiruv ----------
Say ""
Say "4) MT5 tekshiruvi..."
Say ""
$dataDir = Join-Path $root "quant\data"
Set-Location $dataDir
& $py check_setup.py

Say ""
Say "============================================================" "Cyan"
Say "  KEYINGI QADAM" "Cyan"
Say "============================================================" "Cyan"
Say ""
Say "  Yuqorida hammasi [OK] bo'lsa, ma'lumot eksport qiling:" "White"
Say ""
Say "     cd `"$dataDir`"" "Yellow"
Say "     $py export_mt5.py" "Yellow"
Say ""
Say "  Xato bo'lsa — yuqoridagi matnni nusxalab menga yuboring." "White"
Say ""
Read-Host "Yopish uchun Enter bosing"
