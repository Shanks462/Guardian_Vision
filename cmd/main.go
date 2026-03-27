package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"os/exec"
	"sync"
)

type Event struct {
	Camera     string
	Time       float64
	Event      string
	Confidence float64
}

func streamEvent(id int) (<-chan Event, error) {
	cmd := exec.Command("python3", "MahilAi/main.py", fmt.Sprintf("%d", id))

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
			var e Event
			err := json.Unmarshal(scanner.Bytes(), &e)
			if err == nil {
				ch <- e
			}
		}
	}()

	return ch, nil
}

func merge(channels ...<-chan Event) <-chan Event {
	out := make(chan Event)
	var wg sync.WaitGroup

	for _, ch := range channels {
		wg.Add(1)
		go func(c <-chan Event) {
			defer wg.Done()
			for e := range c {
				out <- e
			}
		}(ch)
	}

	go func() {
		wg.Wait()
		close(out)
	}()

	return out
}

func main() {
	numInstances := 4
	var channels []<-chan Event

	for i := 0; i < numInstances; i++ {
		ch, err := streamEvent(i)
		if err != nil {
			panic(err)
		}
		channels = append(channels, ch)
	}

	merged := merge(channels...)

	for e := range merged {
		fmt.Printf("Camera: %s | Event: %s | Confidence: %.2f\n",
			e.Camera, e.Event, e.Confidence)
	}
}