package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"os/exec"
)

type Event struct {
	Camera     string
	Time       float64
	Event      string
	Confidence float64
}

func streamEvent() (<-chan Event, error) {
	cmd := exec.Command("python3", "mai.py")
	stdout, err := cmd.StdoutPipe()
	if err != nil {
		return nil, err
	}

	ch := make(chan Event)
	if err := cmd.Start(); err != nil {
		return nil, err
	}

	go func() {
		defer close(ch)
		defer cmd.Wait()
		scanner := bufio.NewScanner(stdout)
		for scanner.Scan() {
			e := Event{}
			err := json.Unmarshal(scanner.Bytes(), &e)
			if err == nil {
				ch <- e
			}
		}
	}()
	return ch, nil
}

func main() {
	ch, _ := streamEvent()

	for e := range ch {
		fmt.Printf("Camera: %s | Event: %s | Confidence: %.2f\n",
			e.Camera, e.Event, e.Confidence)
	}
}