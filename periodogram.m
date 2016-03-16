function periodogram
clear, clc

function note = findNote(freq)
% C=0, C#=1, D=2, Eb=3, E=4, f=5, F#=6, G=7, G#=8, A=9, Bb=10, B=11

c0 = 16.352;

exp = round(12 * log2(freq/c0));

note = mod(exp,12);
end

notes = zeros(1,12);

[x,fs] = audioread('lisa.wav');
whos x
x = x(:,1);             % get the first channel
%xmax = max(abs(x));     % find the maximum value
%x = x/xmax;             % scalling the signal

m = length(x);          % Window length
n = pow2(nextpow2(m));  % Transform length
y = fft(x,n);           % DFT

y = fftshift(y);          % Rearrange y values
f = (-n/2:n/2-1)*(fs/n);  % 0-centered frequency range
%%whos f
power = y.*conj(y)/n;     % 0-centered power

f = abs(f);
noFreq = length(f);
%%whos noFreq
%start = ceil(noFreq/2);

for i = 1:noFreq
    freq = f(i);
    if (freq ~= 0)
        note = findNote(freq);
        notes(note+1) = notes(note+1)+power(i);
    end
end

% plot(f, power)
% axis([0 1000 0 100])
% grid on
% xlabel('Frequency (Hz)')
% ylabel('Power')
% title('{\bf Periodogram}')
notes

end